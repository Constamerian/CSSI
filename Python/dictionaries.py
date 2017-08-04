sandwich = [["rye", "sourdough", "baguette"],
            [["ham", "salami", "turkey"], ["swiss", "munster", "cheddar"]],
            ["mayo", "mustard", "tabasco"]]

#sandwich[0][1] = sourdough
#sandwich[1] = [["ham", "salami", "turkey"], ["swiss", "munster", "cheddar"]]
#sandwich[1][0][0] = ham

#["mayo", "mustard", "tabasco"] = sandwich[2]
#"cheddar" = sandwich[1][1][2]
#"sourdough" = sandwich[0][1]



city_info = {'new_york' : { 'mayor' : "Bill DeBlasio",
                            'population' : 8406000,
                            'website' : "http://www.nyc.gov"
                            },
             'los_angeles' : { 'mayor' : "Eric Garcetti",
                            'population' : 3884307,
                            'website' : "http://www.lacity.org"
                            },
             'miami' : { 'mayor' : "Tomas Regalado",
                            'population' : 417650,
                            'website' : "http://www.miamigov.com"
                            },
             'chicago' : { 'mayor' : "Rahm Emanuel",
                            'population' : 2719000,
                            'website' : "http://www.cityofchicago.org/"
                            }
        }

#city_info["los_angeles"] = { 'mayor' : "Eric Garcetti",
#                             'population' : 3884307,
#                             'website' : "http://www.lacity.org"
#                             },
#city_info["chicago"]["mayor"] = Rahm Emanuel

#population of New York = city_info["new_york"]["population"]
#the website for Miami city government = city_info["miami"]["website"]
#the mayor of Los Angeles = city_info["los_angeles"]["mayor"]
#a dictionary with all information on chicago = city_info["chicago"]

for cityname in city_info:
    for information in city_info[cityname]:
        print "The " + information + " of" + cityname + " is {}".format(city_info[cityname][information])
