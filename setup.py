from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    requirement_lst:list[str]=[]
    try:
       with open('requirements.txt','r') as file:
           lines=file.readlines()
           for line in lines:
               requirement=line.strip()
               #ignore the empty line and -e.
               if requirement and requirement !='-e .':
                   requirement_lst.append(requirement)
                   
    except FileNotFoundError:
        print("requirements.txt file not founds")  
    return requirement_lst    
        
print(get_requirements()) 

setup(
    name='networkSecurity',
    version='0.0.1',
    author='Ashik Hasan Redoy',
    author_email='ashikhasanhredoy@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)                    