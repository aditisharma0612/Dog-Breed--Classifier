def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    results_stats_dic = {}
    n_images = 0 # Z number of images
    n_dogs_img = 0 # B number of dog images
    n_notdogs_img = 0 # C number of NON-dog images    
    n_match = 0 # number of matches between pet & classifier labels    
    n_correct_dogs = 0 # number of correctly classified dog images
    n_correct_notdogs = 0 # D number of correctly classified NON-dog images    
    n_correct_breed = 0 # E number of correctly classified dog breeds    
    pct_match = 0 # percentage of correct matches
    pct_correct_dogs = 0 # percentage of correctly classified dogs
    pct_correct_breed = 0 # percentage of correctly classified dog breeds
    pct_correct_notdogs = 0 # percentage of correctly classified NON-dogs
    
    for test_file in results_dic.keys():
        test_item = results_dic[test_file]
        n_images += 1 # Z
        n_dogs_img += test_item[3] # B
        n_match += test_item[2]
        n_correct_dogs += test_item[3] and test_item[4]
        n_correct_notdogs += (not test_item[3]) and (not test_item[4])
        n_correct_breed += test_item[3] and test_item[2]        
    n_notdogs_img = n_images - n_dogs_img

    pct_match = n_match/n_images*100
    pct_correct_dogs = n_correct_dogs/n_dogs_img*100
    pct_correct_breed = n_correct_breed/n_dogs_img*100
    pct_correct_notdogs = n_correct_notdogs/n_notdogs_img*100

    results_stats_dic = {\
    'n_images':n_images,\
    'n_dogs_img':n_dogs_img,\
    'n_notdogs_img':n_notdogs_img,\
    'n_match':n_match,\
    'n_correct_dogs':n_correct_dogs,\
    'n_correct_notdogs':n_correct_notdogs,\
    'n_correct_breed':n_correct_breed,\
    'pct_match':pct_match,\
    'pct_correct_dogs':pct_correct_dogs,\
    'pct_correct_breed':pct_correct_breed,\
    'pct_correct_notdogs':pct_correct_notdogs}
        
   
    return results_stats_dic
