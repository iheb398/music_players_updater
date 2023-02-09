# music_players_updater
/**
   Player Developer tech assignment
  
  @verbatim
  ******************************************************************************
  * @file    readme.txt 
  * @author  Iheb Ouni	
  * @mail    ing.iheb.ouni@gmail.com
  * @brief   Description of the Player Developer tech assignment.
  ******************************************************************************
  


update_music_players is the main function that takes in the file path, client ID, and token as arguments.
The function first reads the CSV file and stores the MAC addresses in a list. It then defines the endadress, request headers, and request body. 
Finally, it iterates over the MAC addresses, replaces the placeholder in the endpoint with the MAC address,
sends a PUT request to the API, and checks the response status code. 
If the response status code is 200, it prints the response body. If the response status code is one of the error codes (401, 404, 409, 500), 
it prints an error message.

Technical Decisions:

The programming language chosen for this task is Python as it is widely used for data processing, REST API integrations, 
and has a vast library for CSV processing.
A CSV reader library will be used to parse the .csv file, and the data will be stored in a dictionary data structure for easy access.
The requests library in Python will be used to make REST API calls to update the software version on each music player.
A separate function will be written to handle API requests, and it will return the response status code and error message in case of any errors.



