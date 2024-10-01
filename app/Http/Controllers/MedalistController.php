<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Medalist; // Ensure to include the Medalist model
use Illuminate\Support\Facades\Storage;
use League\Csv\Reader; // Ensure you have installed league/csv

class MedalistController extends Controller
{
    // Upload Endpoint
    public function upload(Request $request)
    {
        try {
            $request->validate(['file' => 'required|mimes:csv,txt']);

            // Store the uploaded file
            $path = $request->file('file')->store('medalists');

            // Process the CSV file
            $csv = Reader::createFromPath(storage_path("app/{$path}"), 'r');
            $csv->setHeaderOffset(0); // Set the CSV header offset

            foreach ($csv as $row) {
                Medalist::create([
                    'name' => $row['name'],
                    'medal_type' => $row['medal_type'],
                    'gender' => $row['gender'],
                    'country' => $row['country'],
                    'country_code' => $row['country_code'],
                    'nationality' => $row['nationality'],
                    'medal_code' => $row['medal_code'],
                    'medal_date' => $row['medal_date'],
                ]);
            }

            return response()->json(['message' => 'File uploaded successfully.']);
        } catch (\Exception $e) {
            return response()->json(['error' => $e->getMessage()], 500);
        }
    }



    // Get Event Aggregate Stats Endpoint
    public function getEventAggregateStats()
    {
        $medalists = Medalist::all()->groupBy('event'); 

        // Transform data into the required format
        $data = [];
        foreach ($medalists as $event => $medalistsGroup) {
            $data[] = [
                'discipline' => $event, 
                'event' => $event,
                'event_date' => '', 
                'medalists' => $medalistsGroup->toArray(),
            ];
        }

        return response()->json([
            'data' => $data,
            'paginate' => [
                'current_page' => 1,
                'total_pages' => 1,
                'next_page' => null,
                'previous_page' => null,
            ],
        ]);
    }
}
