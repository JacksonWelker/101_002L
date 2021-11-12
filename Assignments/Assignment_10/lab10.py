def wordcount():
    pass
    while True:
       try:
        i = input('Enter the name of the file to open')
        i = open(i)
    except IOError:
        print("Could not open file", i)
    finally:
           pass.close
    
    
    file = open(i,"r")
    frequent_word = ""
    frequency = 0 
    words = []
 

    for line in file:
        line_word = line.lower().replace(',','').replace('.','').split(" "); 
    for w in line_word: 
        words.append(w); 
    for i in range(0, len(words)):
        count = 1; 
     
    for j in range(i+1, len(words)): 
        if(words[i] == words[j]): 
            count = count + 1; 
 
    if(count > frequency): 
        frequency = count; 
        frequent_word = words[i]; 
 
    print("Most repeated word: " + frequent_word)
    print("Frequency: " + str(frequency))
    file.close();