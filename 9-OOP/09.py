#Static Methods in Python

class ChaiUtils:

    @staticmethod
    def cleaningredients(text):
       return  [ item.strip() for item in text.split(",")]  #slpit() method slpits the text string based on commas
    #strip() method reomves the extra spaces or cleans up the edges


raw = "  water,  pepper , milk,   ginger"

# obj = ChaiUtils()           
# i = obj.cleaningredients(raw)   -- to do this , you need to write self in the function cleaningreidients
# print(i)

#but when we write staticmethod , then we can directly use the function with class name
cleaned = ChaiUtils.cleaningredients(raw)
print(cleaned)