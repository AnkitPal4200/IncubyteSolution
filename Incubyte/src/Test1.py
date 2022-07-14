from Logger import Logger
class Test1:
    def leap_year(self,year):
        logger =Logger()
        op=logger.log()
        print(op)
        if year%400==0:
            return True
        elif year%4==0 and year%100!=0:
            return True
        return False
