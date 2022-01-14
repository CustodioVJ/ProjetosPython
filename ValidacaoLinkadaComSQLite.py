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
   "version": 3
  },
  "orig_nbformat": 2
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "\n",
    "\n",
    "a = input(\"Digite sua senha: \")\n",
    "conn = sqlite3.connect('agenda.db')\n",
    "cursor = conn.cursor()\n",
    "cursor.execute(\"\"\"SELECT * Login FROM Senha \"\"\")\n",
    "\n",
    "for row in cursor.fletchall():\n",
    "    if row[0]==a:\n",
    "        print('Acesso liberado')\n",
    "\n",
    "        else: print ('Acesso negado')\n",
    "         conn.close()"
   ]
  }
 ]
}
