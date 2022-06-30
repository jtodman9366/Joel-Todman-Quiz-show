print(r"""
   .-')                      (`-.              ('-.    .-')              .-') _                     ('-. .-. .-') _   ,---. 
( '.( OO )_                  _(OO  )_          _(  OO)  ( OO ).           ( OO ) )                   ( OO )  /(  OO) )  |   | 
 ,--.   ,--.).-'),-----. ,--(_/   ,. \ ,-.-') (,------.(_)---\_)      ,--./ ,--,' ,-.-')   ,----.    ,--. ,--./     '._ |   | 
 |   `.'   |( OO'  .-.  '\   \   /(__/ |  |OO) |  .---'/    _ |       |   \ |  |\ |  |OO) '  .-./-') |  | |  ||'--...__)|   | 
 |         |/   |  | |  | \   \ /   /  |  |  \ |  |    \  :` `.       |    \|  | )|  |  \ |  |_( O- )|   .|  |'--.  .--'|   | 
 |  |'.'|  |\_) |  |\|  |  \   '   /,  |  |(_/(|  '--.  '..`''.)      |  .     |/ |  |(_/ |  | .--, \|       |   |  |   |  .' 
 |  |   |  |  \ |  | |  |   \     /__),|  |_.' |  .--' .-._)   \      |  |\    | ,|  |_.'(|  | '. (_/|  .-.  |   |  |   `--'  
 |  |   |  |   `'  '-'  '    \   /   (_|  |    |  `---.\       /      |  | \   |(_|  |    |  '--'  | |  | |  |   |  |   .--.  
 `--'   `--'     `-----'      `-'      `--'    `------' `-----'       `--'  `--'  `--'     `------'  `--' `--'   `--'   '--'  
 """)


print("Welcome to movie time! you will answer a few True and False questions. Please only enter T or F when its your time to answer. Have Fun!")
print()

# The quiz question and answers in two tupals
questions = ('Q1. Friday and Saturday nights are the best time to go to the movies', 'Q2. Star Wars was a bad movie', 'Q3. Going to the movies is fun!')
answers = ('T', 'F', 'T')

#determine the number of questions, using len function
numberOfQuestions = len(questions)
score = 0
# for loop, using the range function
for index in range(numberOfQuestions):
  guess = input(f" {questions[index]} please Enter T or F: ")
  if guess == answers[index]:
    score +=1
  if guess != answers[index]:
    input(f" {questions[index]} please Enter T or F: ")
#print out the number of questions the user got right....
print(f"you have {score} out of 3 correct...Thanks for playing")










