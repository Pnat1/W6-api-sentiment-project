{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4d539542",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[31mERROR: Could not find a version that satisfies the requirement config.configuration\u001b[0m\n",
      "\u001b[31mERROR: No matching distribution found for config.configuration\u001b[0m\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install config.configuration\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "18cf9b7d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'config.configuration'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-9-2b26c8bcc880>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mrecord\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconfiguration\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mengine\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtextblob\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mTextBlob\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'config.configuration'"
     ]
    }
   ],
   "source": [
    "import random\n",
    "from numpy import record\n",
    "import pandas as pd\n",
    "from config.configuration import engine\n",
    "from textblob import TextBlob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57dc1d29",
   "metadata": {},
   "outputs": [],
   "source": [
    "def actor_characters():\n",
    "    \"\"\"\n",
    "    Calls the database in MySQl and returns all the actor characters in a json format.\n",
    "    \"\"\"\n",
    "    query = f\"\"\"\n",
    "    SELECT film_character FROM actors;\n",
    "    \"\"\"\n",
    "    data = pd.read_sql_query(query,engine)\n",
    "    return data.to_json(orient=\"records\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36a9eee0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def lines():\n",
    "    \"\"\"\n",
    "    Calls the database in MySQl and returns all the script lines in a json format.\n",
    "    \"\"\"\n",
    "    query= f\"\"\"\n",
    "    SELECT line_quote FROM line_quotes;\n",
    "    \"\"\"\n",
    "    data = pd.read_sql_query(query,engine)\n",
    "    return data.to_json(orient=\"records\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ad60573",
   "metadata": {},
   "outputs": [],
   "source": [
    "def places():\n",
    "    \"\"\"\n",
    "    Calls the database in MySQl and returns the different places where the film_characters \n",
    "    said their lines.\n",
    "    \"\"\"\n",
    "    query = f\"\"\"\n",
    "    SELECT place FROM place;\n",
    "    \"\"\"\n",
    "    data = pd.read_sql_query(query,engine)\n",
    "    return data.to_json(orient='records')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e81a7ba7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def actor_line(actor_name):\n",
    "    \"\"\"\n",
    "    You can put the name of the author you want and this returns his name, the palce\n",
    "    he is in and the script line he says.\n",
    "    \"\"\"\n",
    "    query = f\"\"\"\n",
    "    SELECT film_character, line_quote, place\n",
    "    FROM actors\n",
    "    INNER JOIN line_quote ON actors_actor_id = actor_id\n",
    "    INNER JOIN place ON place_id = place_place_id \n",
    "    WHERE actor_name = '{film_character}';\n",
    "    \"\"\"\n",
    "    data = pd.read_sql_query(query,engine)\n",
    "    return data.to_json(orient=\"records\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddcdf46b",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "0153f1a28eccce8dadf35cb8ebd13799d27f39122d122c76555a19b7b24689d5"
  },
  "kernelspec": {
   "display_name": "ironhack",
   "language": "python",
   "name": "python3"
  },
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
