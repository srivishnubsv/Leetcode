class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temp=[]
        kelvin=celsius+273.15
        Fahrenheit=celsius*1.80+32.00
        temp.append(kelvin)
        temp.append(Fahrenheit)
        return temp
