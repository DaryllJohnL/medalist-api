<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use League\Csv\Reader;

class MedalistController extends Controller
{
    // Upload Endpoint
    public function upload(Request $request)
    {
        try {
            // Validate that a file was uploaded and that it's a CSV or text file
            $request->validate(['file' => 'required|mimes:csv,txt']);

            // Store the uploaded file in the 'medalists' directory within the storage
            $path = $request->file('file')->store('medalists');

            // Log or return success message
            return response()->json([
                'message' => 'File uploaded and stored successfully.',
                'file_path' => $path // Return the file path for your Python watchdog service to watch
            ]);
        } catch (\Exception $e) {
            // If there's an error, return it
            return response()->json(['error' => $e->getMessage()], 500);
        }
    }

    // Get Event Aggregate Stats Endpoint
    public function getEventAggregateStats()
    {
        // As there is no MySQL database anymore, you might not need this function
        // However, you can still implement similar functionality on your MongoDB side using your Python service.
        return response()->json([
            'message' => 'This functionality is now handled by MongoDB and the Python service.'
        ]);
    }
}
