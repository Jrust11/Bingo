print('Enter the dimension of the board: ')
board_dimension = input()
y = True
words = []
board_words =[]
checked_sqaures = 0

x = 1
#Obtains all elements in a n-dimension board
while(x < int(board_dimension)*int(board_dimension)+1):
    element =  'a' #driver.find_element_by_xpath("//a[@id='link']")

    #//*[@id="svg"]/svg/g[1]/g/text/tspan
    #//*[@id="svg"]/svg/g[2]/g/text/tspan
    #//*[@id="svg"]/svg/g[25]/g/text/tspan

    board_words.append(x)
    x=x+1
    print(x)

print(board_words)

while(y == True):

    #Asks for the most recent word or number called
    print('Input the word or number that was just called: ')
    bingo_input = input()
    words.append(bingo_input)

    for words in board_words:

        #Click on the corresponding xml object
        ##element.click()
        #Keeps track of the total squared checked
        checked_sqaures = checked_sqaures + 1
        print(checked_sqaures)


    else:
        print('Not on the board')
