<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Medalist extends Model
{
    use HasFactory;

    // Define fillable fields for mass assignment
    protected $fillable = [
        'name',
        'medal_type',
        'gender',
        'country',
        'country_code',
        'nationality',
        'medal_code',
        'medal_date',
        'event' // Include event if it's a field in your database
    ];

    // You may also define any hidden attributes or casts as needed
}
