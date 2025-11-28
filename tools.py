"""Tools for the trip planner agent."""

# Area Information Database
AREAS_DATABASE = {
    "germany": {
        "name": "Germany",
        "description": "A country in Central Europe known for its rich history, beautiful landscapes, and vibrant cities.",
        "best_season": "May to September",
        "weather": "Temperate climate with warm summers and cold winters",
        "highlights": ["Berlin's historic sites", "Bavarian Alps", "Neuschwanstein Castle", "Black Forest", "Rhine Valley"],
        "culture": "Rich in history, art, music, and beer culture",
        "cuisine": "Famous for sausages, pretzels, beer, and hearty dishes",
        "activities": "Historical tours, hiking, wine tasting, Christmas markets",
        "budget_level": "Moderate to high",
        "language": "German",
        "currency": "Euro (EUR)"
    },
    "switzerland": {
        "name": "Switzerland",
        "description": "A landlocked country in Central Europe famous for its mountains, lakes, and precision.",
        "best_season": "June to September (summer), December to March (winter sports)",
        "weather": "Alpine climate with cold winters and mild summers",
        "highlights": ["Swiss Alps", "Matterhorn", "Lake Geneva", "Zurich", "Interlaken", "Jungfraujoch"],
        "culture": "Multilingual country with German, French, Italian, and Romansh",
        "cuisine": "Fondue, raclette, chocolate, cheese, rösti",
        "activities": "Skiing, hiking, mountain climbing, lake cruises, chocolate factory tours",
        "budget_level": "High",
        "language": "German, French, Italian, Romansh",
        "currency": "Swiss Franc (CHF)"
    },
    "saudi arabia": {
        "name": "Saudi Arabia",
        "description": "A Middle Eastern country known for its rich Islamic heritage, modern cities, and desert landscapes.",
        "best_season": "November to March (cooler months)",
        "weather": "Desert climate with very hot summers and mild winters",
        "highlights": ["Mecca and Medina (holy cities)", "Riyadh", "Jeddah", "Al-Ula", "Red Sea coast", "Diriyah"],
        "culture": "Deep Islamic traditions, Bedouin heritage, modern transformation",
        "cuisine": "Kabsa, shawarma, dates, Arabic coffee, traditional sweets",
        "activities": "Religious pilgrimage, desert safaris, diving in Red Sea, historical sites, modern shopping",
        "budget_level": "Moderate to high",
        "language": "Arabic",
        "currency": "Saudi Riyal (SAR)"
    },
    "dubai": {
        "name": "Dubai",
        "description": "A modern metropolis in the UAE known for luxury, skyscrapers, and world-class attractions.",
        "best_season": "November to April (winter months)",
        "weather": "Desert climate with extremely hot summers and warm winters",
        "highlights": ["Burj Khalifa", "Palm Jumeirah", "Dubai Mall", "Burj Al Arab", "Dubai Marina", "Desert Safari"],
        "culture": "Modern Emirati culture with international influences",
        "cuisine": "Arabic, Middle Eastern, and international cuisine",
        "activities": "Shopping, luxury experiences, desert safaris, water parks, skydiving, fine dining",
        "budget_level": "High",
        "language": "Arabic, English widely spoken",
        "currency": "UAE Dirham (AED)"
    },
    "poland": {
        "name": "Poland",
        "description": "A Central European country with medieval architecture, rich history, and beautiful countryside.",
        "best_season": "May to September",
        "weather": "Temperate climate with cold winters and warm summers",
        "highlights": ["Krakow Old Town", "Warsaw", "Auschwitz-Birkenau", "Wieliczka Salt Mine", "Tatra Mountains"],
        "culture": "Rich Slavic traditions, strong Catholic heritage, resilient history",
        "cuisine": "Pierogi, bigos, kielbasa, żurek, traditional Polish dishes",
        "activities": "Historical tours, hiking in mountains, cultural festivals, castle visits",
        "budget_level": "Low to moderate",
        "language": "Polish",
        "currency": "Polish Zloty (PLN)"
    },
    "china": {
        "name": "China",
        "description": "A vast country in East Asia with ancient history, diverse landscapes, and modern cities.",
        "best_season": "April to May, September to October",
        "weather": "Varies greatly by region - from tropical to subarctic",
        "highlights": ["Great Wall of China", "Forbidden City", "Terracotta Army", "Shanghai", "Guilin", "Tibet"],
        "culture": "Ancient civilization with rich traditions, philosophy, and arts",
        "cuisine": "Diverse regional cuisines including Sichuan, Cantonese, Beijing duck, dim sum",
        "activities": "Historical sites, hiking, cultural experiences, modern city exploration, nature tours",
        "budget_level": "Low to moderate",
        "language": "Mandarin Chinese",
        "currency": "Chinese Yuan (CNY)"
    }
}

# Flights Database
FLIGHTS_DATABASE = {
    "qatar_airways": {
        "airline": "Qatar Airways",
        "class": "Luxury",
        "description": "Premium airline known for exceptional service and luxury amenities",
        "price_range": "$800 - $2000",
        "features": ["Qsuite business class", "World-class dining", "Onboard entertainment", "Lounge access", "Priority boarding"],
        "best_for": "Luxury travelers, business class passengers, long-haul flights",
        "destinations": "Connects to all major destinations worldwide"
    },
    "saudi_airlines": {
        "airline": "Saudi Airlines",
        "class": "Luxury to Economy",
        "description": "National carrier of Saudi Arabia with modern fleet and good service",
        "price_range": "$600 - $1500",
        "features": ["Modern aircraft", "Halal meals", "Good entertainment system", "Comfortable seating", "Reliable service"],
        "best_for": "Travelers to Middle East, families, business travelers",
        "destinations": "Extensive network in Middle East, Asia, Europe, and Americas"
    },
    "wizz_air": {
        "airline": "Wizz Air",
        "class": "Economy",
        "description": "Low-cost European airline offering affordable flights",
        "price_range": "$50 - $300",
        "features": ["Budget-friendly", "Point-to-point flights", "Online check-in", "Optional extras available"],
        "best_for": "Budget travelers, short trips, European destinations",
        "destinations": "Primarily Europe and some Middle Eastern destinations"
    },
    "flydubai": {
        "airline": "FlyDubai",
        "class": "Economy",
        "description": "Low-cost airline based in Dubai, part of Emirates Group",
        "price_range": "$100 - $500",
        "features": ["Affordable fares", "Modern fleet", "Good connectivity", "Dubai hub", "Flexible booking"],
        "best_for": "Budget travelers, Dubai connections, regional travel",
        "destinations": "Middle East, Africa, Asia, and Europe"
    },
    "emirates": {
        "airline": "Emirates",
        "class": "Luxury to Economy",
        "description": "Premium airline with excellent service and modern aircraft",
        "price_range": "$700 - $2500",
        "features": ["A380 aircraft", "ICE entertainment system", "Excellent service", "Dubai hub", "Comfortable seating"],
        "best_for": "Long-haul travelers, luxury seekers, Dubai connections",
        "destinations": "Global network with Dubai as hub"
    }
}

# Activities Database
ACTIVITIES_DATABASE = {
    "germany": [
        {
            "name": "Berlin Historical Tour",
            "type": "Cultural",
            "duration": "4-6 hours",
            "price": "€50-80",
            "description": "Explore Berlin's historic sites including Brandenburg Gate, Berlin Wall, and Reichstag Building"
        },
        {
            "name": "Bavarian Alps Hiking",
            "type": "Adventure",
            "duration": "Full day",
            "price": "€60-100",
            "description": "Scenic hiking trails in the Bavarian Alps with stunning mountain views"
        },
        {
            "name": "Neuschwanstein Castle Visit",
            "type": "Cultural",
            "duration": "3-4 hours",
            "price": "€40-60",
            "description": "Visit the fairy-tale castle that inspired Disney's Sleeping Beauty Castle"
        },
        {
            "name": "Rhine Valley Wine Tasting",
            "type": "Food & Drink",
            "duration": "Half day",
            "price": "€70-120",
            "description": "Wine tasting tour through the beautiful Rhine Valley vineyards"
        },
        {
            "name": "Black Forest Tour",
            "type": "Nature",
            "duration": "Full day",
            "price": "€80-150",
            "description": "Explore the famous Black Forest with its charming villages and cuckoo clocks"
        }
    ],
    "switzerland": [
        {
            "name": "Jungfraujoch - Top of Europe",
            "type": "Adventure",
            "duration": "Full day",
            "price": "CHF 180-220",
            "description": "Take a train to the highest railway station in Europe with breathtaking Alpine views"
        },
        {
            "name": "Swiss Chocolate Factory Tour",
            "type": "Food & Drink",
            "duration": "2-3 hours",
            "price": "CHF 25-40",
            "description": "Learn about Swiss chocolate making and enjoy tastings at a traditional factory"
        },
        {
            "name": "Lake Geneva Cruise",
            "type": "Sightseeing",
            "duration": "2-4 hours",
            "price": "CHF 30-60",
            "description": "Scenic boat cruise on Lake Geneva with views of the Alps and charming lakeside towns"
        },
        {
            "name": "Matterhorn Viewing",
            "type": "Nature",
            "duration": "Half day",
            "price": "CHF 50-80",
            "description": "Visit Zermatt and see the iconic Matterhorn mountain"
        },
        {
            "name": "Swiss Alps Skiing",
            "type": "Adventure",
            "duration": "Full day",
            "price": "CHF 60-120",
            "description": "World-class skiing in the Swiss Alps with various difficulty levels"
        }
    ],
    "saudi arabia": [
        {
            "name": "Desert Safari Experience",
            "type": "Adventure",
            "duration": "Half day",
            "price": "SAR 200-400",
            "description": "Dune bashing, camel riding, and traditional Bedouin camp experience"
        },
        {
            "name": "Al-Ula Historical Tour",
            "type": "Cultural",
            "duration": "Full day",
            "price": "SAR 300-500",
            "description": "Explore ancient Nabatean ruins and stunning rock formations in Al-Ula"
        },
        {
            "name": "Red Sea Diving",
            "type": "Adventure",
            "duration": "Half day",
            "price": "SAR 250-450",
            "description": "Scuba diving or snorkeling in the pristine Red Sea waters"
        },
        {
            "name": "Diriyah Heritage Tour",
            "type": "Cultural",
            "duration": "3-4 hours",
            "price": "SAR 100-200",
            "description": "Visit the historic Diriyah, the birthplace of the Saudi kingdom"
        },
        {
            "name": "Traditional Arabic Dinner",
            "type": "Food & Drink",
            "duration": "2-3 hours",
            "price": "SAR 150-300",
            "description": "Authentic Saudi cuisine experience with traditional music and entertainment"
        }
    ],
    "dubai": [
        {
            "name": "Burj Khalifa Observation Deck",
            "type": "Sightseeing",
            "duration": "1-2 hours",
            "price": "AED 150-300",
            "description": "Visit the world's tallest building and enjoy panoramic views of Dubai"
        },
        {
            "name": "Desert Safari with BBQ Dinner",
            "type": "Adventure",
            "duration": "Evening (4-5 hours)",
            "price": "AED 200-400",
            "description": "Dune bashing, camel rides, sandboarding, and traditional dinner under the stars"
        },
        {
            "name": "Palm Jumeirah Tour",
            "type": "Sightseeing",
            "duration": "2-3 hours",
            "price": "AED 100-200",
            "description": "Explore the iconic man-made Palm Island and Atlantis resort"
        },
        {
            "name": "Dubai Mall Shopping",
            "type": "Shopping",
            "duration": "Flexible",
            "price": "Varies",
            "description": "World's largest shopping mall with over 1,200 stores and Dubai Aquarium"
        },
        {
            "name": "Dubai Marina Dhow Cruise",
            "type": "Sightseeing",
            "duration": "2 hours",
            "price": "AED 100-250",
            "description": "Traditional dhow boat cruise with dinner and views of modern Dubai skyline"
        }
    ],
    "poland": [
        {
            "name": "Krakow Old Town Walking Tour",
            "type": "Cultural",
            "duration": "2-3 hours",
            "price": "PLN 50-100",
            "description": "Explore the medieval Old Town, Main Market Square, and Wawel Castle"
        },
        {
            "name": "Auschwitz-Birkenau Memorial",
            "type": "Historical",
            "duration": "Half day",
            "price": "PLN 80-150",
            "description": "Visit the former concentration camp, now a memorial and museum"
        },
        {
            "name": "Wieliczka Salt Mine Tour",
            "type": "Cultural",
            "duration": "2-3 hours",
            "price": "PLN 80-120",
            "description": "Underground tour of the historic salt mine with stunning salt sculptures"
        },
        {
            "name": "Tatra Mountains Hiking",
            "type": "Adventure",
            "duration": "Full day",
            "price": "PLN 100-200",
            "description": "Hiking in the beautiful Tatra Mountains with scenic trails"
        },
        {
            "name": "Polish Food Tour",
            "type": "Food & Drink",
            "duration": "3-4 hours",
            "price": "PLN 150-250",
            "description": "Taste traditional Polish cuisine including pierogi, bigos, and local specialties"
        }
    ],
    "china": [
        {
            "name": "Great Wall of China Tour",
            "type": "Historical",
            "duration": "Full day",
            "price": "CNY 300-600",
            "description": "Visit one of the world's most iconic landmarks with hiking options"
        },
        {
            "name": "Forbidden City Exploration",
            "type": "Cultural",
            "duration": "3-4 hours",
            "price": "CNY 60-100",
            "description": "Explore the ancient imperial palace complex in Beijing"
        },
        {
            "name": "Terracotta Army Visit",
            "type": "Historical",
            "duration": "Half day",
            "price": "CNY 150-250",
            "description": "See the incredible Terracotta Warriors in Xi'an"
        },
        {
            "name": "Guilin Li River Cruise",
            "type": "Nature",
            "duration": "Full day",
            "price": "CNY 400-800",
            "description": "Scenic cruise through stunning karst mountain landscapes"
        },
        {
            "name": "Traditional Chinese Tea Ceremony",
            "type": "Cultural",
            "duration": "1-2 hours",
            "price": "CNY 100-200",
            "description": "Experience authentic Chinese tea culture and ceremony"
        }
    ]
}


def get_area_information(area_name: str = None, user_preferences: str = None) -> str:
    """Get information about travel destinations. 
    The database contains information about Germany, Switzerland, Saudi Arabia, Dubai, Poland, and China.
    The agent should choose the best destination based on user needs and preferences.
    If no area is specified, returns information about all available areas."""
    
    area_name = area_name.strip().lower() if area_name else None
    
    # If specific area requested
    if area_name:
        # Try to find the area
        area = None
        for key in AREAS_DATABASE.keys():
            if area_name in key or key in area_name:
                area = AREAS_DATABASE[key]
                break
        
        if not area:
            available = ", ".join([area["name"] for area in AREAS_DATABASE.values()])
            return f"Area '{area_name}' not found in database.\n\nAvailable destinations: {available}\n\nPlease specify one of these destinations."
        
        # Return formatted area information
        info = f"🌍 Destination: {area['name']}\n\n"
        info += f"📝 Description:\n{area['description']}\n\n"
        info += f"🌤️ Best Season: {area['best_season']}\n"
        info += f"🌡️ Weather: {area['weather']}\n\n"
        info += f"⭐ Highlights:\n"
        for highlight in area['highlights']:
            info += f"  • {highlight}\n"
        info += f"\n🏛️ Culture: {area['culture']}\n"
        info += f"🍽️ Cuisine: {area['cuisine']}\n"
        info += f"🎯 Activities: {area['activities']}\n"
        info += f"💰 Budget Level: {area['budget_level']}\n"
        info += f"🗣️ Language: {area['language']}\n"
        info += f"💵 Currency: {area['currency']}\n"
        
        return info
    
    # If no specific area, return summary of all areas
    info = "🌍 Available Travel Destinations:\n\n"
    for key, area in AREAS_DATABASE.items():
        info += f"📍 {area['name']}\n"
        info += f"   {area['description'][:100]}...\n"
        info += f"   Best Season: {area['best_season']}\n"
        info += f"   Budget: {area['budget_level']}\n\n"
    
    if user_preferences:
        info += f"\n💡 Based on your preferences: {user_preferences}\n"
        info += "I can help you choose the best destination that matches your needs!\n"
    
    return info


def get_flight_options(destination: str = None, budget: str = None, preferences: str = None) -> str:
    """Get flight options from various airlines.
    Available airlines: Qatar Airways (luxury), Saudi Airlines, Wizz Air (economy), FlyDubai (economy), Emirates.
    Prices are shown for each airline. The agent should recommend the best flight based on user needs."""
    
    info = "✈️ Available Flight Options:\n\n"
    
    for key, flight in FLIGHTS_DATABASE.items():
        info += f"🛫 {flight['airline']}\n"
        info += f"   Class: {flight['class']}\n"
        info += f"   Price Range: {flight['price_range']}\n"
        info += f"   Description: {flight['description']}\n"
        info += f"   Features:\n"
        for feature in flight['features']:
            info += f"     • {feature}\n"
        info += f"   Best For: {flight['best_for']}\n"
        info += f"   Destinations: {flight['destinations']}\n\n"
    
    if destination:
        info += f"\n📍 Destination: {destination}\n"
    if budget:
        info += f"💰 Budget: {budget}\n"
    if preferences:
        info += f"💡 Preferences: {preferences}\n"
        info += "\nI can help you choose the best airline based on your budget and preferences!\n"
    
    return info


def get_activities(destination: str, activity_type: str = None, budget: str = None) -> str:
    """Get available activities for a specific destination.
    The database contains various activities for each destination including cultural, adventure, food, nature, and sightseeing options.
    The agent should choose appropriate activities based on user interests and destination."""
    
    destination = destination.strip().lower() if destination else None
    
    if not destination:
        return "Please specify a destination to see available activities.\n\nAvailable destinations: Germany, Switzerland, Saudi Arabia, Dubai, Poland, China"
    
    # Find the destination
    area_key = None
    for key in AREAS_DATABASE.keys():
        if destination in key or key in destination:
            area_key = key
            break
    
    if not area_key:
        available = ", ".join([area["name"] for area in AREAS_DATABASE.values()])
        return f"Destination '{destination}' not found.\n\nAvailable destinations: {available}"
    
    # Get activities for the destination
    activities = ACTIVITIES_DATABASE.get(area_key, [])
    
    if not activities:
        return f"No activities found for {AREAS_DATABASE[area_key]['name']}"
    
    info = f"🎯 Available Activities in {AREAS_DATABASE[area_key]['name']}:\n\n"
    
    # Filter by activity type if specified
    filtered_activities = activities
    if activity_type:
        activity_type_lower = activity_type.lower()
        filtered_activities = [a for a in activities if activity_type_lower in a['type'].lower()]
        if filtered_activities:
            info += f"Filtered by type: {activity_type}\n\n"
    
    for i, activity in enumerate(filtered_activities, 1):
        info += f"{i}. {activity['name']}\n"
        info += f"   Type: {activity['type']}\n"
        info += f"   Duration: {activity['duration']}\n"
        info += f"   Price: {activity['price']}\n"
        info += f"   Description: {activity['description']}\n\n"
    
    if not filtered_activities and activity_type:
        info = f"No {activity_type} activities found for {AREAS_DATABASE[area_key]['name']}.\n\n"
        info += "Available activity types: "
        types = set([a['type'] for a in activities])
        info += ", ".join(types)
    
    if budget:
        info += f"\n💰 Budget consideration: {budget}\n"
        info += "I can help you select activities that fit your budget!\n"
    
    return info
