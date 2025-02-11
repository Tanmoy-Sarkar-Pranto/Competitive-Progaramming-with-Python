url = {
  "@context": "https://schema.org",
  "@id": "https://www.example.com/#breadcrump",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": "https://www.example.com/",      
      "name": "Home"       
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": "https://www.example.com/real-estate/",
      "name": "Real estate"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": "https://www.example.com/en/paris/",
      "name": "Paris"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "item": "https://www.example.com/en/paris/apartment/",
      "name": "Apartment"
    },
    {
     "@type": "ListItem",
     "position": 5,
     "item": "https://www.example.com/en/paris/apartment/affordable",
     "name": "Affordable rentals Paris"      
    }
  ]
}

print(url.items())
