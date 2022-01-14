{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.4"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.9.4 64-bit",
   "metadata": {
    "interpreter": {
     "hash": "6ff2b6a8c199887330d38400c230fc185af08e9b570fc128bcd902273b11080c"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<selenium.webdriver.remote.webelement.WebElement (session=\"5e72c9fe451149ee19ceec81db6604f8\", element=\"29a92cc3-07bb-4d75-81a3-8415cf71ecce\")>"
      ]
     },
     "metadata": {},
     "execution_count": 9
    }
   ],
   "source": [
    "from selenium import webdriver\n",
    "navegador = webdriver.Chrome()\n",
    "\n",
    "navegador.get(\"https://www.magazinevoce.com.br/magazineofertamagazinne/\")\n",
    "navegador.find_element_by_xpath('//*[@id=\"h\"]/div[1]/ul/li[5]/a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}
