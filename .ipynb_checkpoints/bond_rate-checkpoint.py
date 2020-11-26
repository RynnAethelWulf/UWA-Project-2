{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-10-09T11:43:08.394070Z",
     "start_time": "2020-10-09T11:43:08.374069Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0.0595,\n",
       " 0.0681,\n",
       " 0.0615,\n",
       " 0.0578,\n",
       " 0.0836,\n",
       " 0.095,\n",
       " 0.1,\n",
       " 0.1041,\n",
       " 0.095,\n",
       " 0.088,\n",
       " 0.1008,\n",
       " 0.126,\n",
       " 0.15,\n",
       " 0.14,\n",
       " 0.135,\n",
       " 0.134,\n",
       " 0.1485,\n",
       " 0.134,\n",
       " 0.1285,\n",
       " 0.1295,\n",
       " 0.129,\n",
       " 0.1207,\n",
       " 0.0939,\n",
       " 0.0894,\n",
       " 0.0668,\n",
       " 0.1004,\n",
       " 0.0825,\n",
       " 0.0732,\n",
       " 0.0614,\n",
       " 0.0485,\n",
       " 0.0674,\n",
       " 0.0554,\n",
       " 0.0582,\n",
       " 0.054,\n",
       " 0.0576,\n",
       " 0.0523,\n",
       " 0.0535,\n",
       " 0.057,\n",
       " 0.0621,\n",
       " 0.0422,\n",
       " 0.0547,\n",
       " 0.0556,\n",
       " 0.0383,\n",
       " 0.0323,\n",
       " 0.042425,\n",
       " 0.02955,\n",
       " 0.02845,\n",
       " 0.027925,\n",
       " 0.0258,\n",
       " 0.0243,\n",
       " 0.012]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import csv\n",
    "with open ( '../Financial-Analysis-of-AAPL--Apple-Co-/10yr Bond Rates.csv',encoding=\"utf8\") as data_file:\n",
    "    data = csv.DictReader(data_file)\n",
    "    bond_10_yr_69_2019 = []\n",
    "    for rows in data:\n",
    "        if rows['date'][:3] == 'Dec':\n",
    "            bond_10_yr_69_2019.append(round(float(rows['value'])/100,6))\n",
    "bond_10_yr_69_2019"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-10-09T11:39:33.220025Z",
     "start_time": "2020-10-09T11:39:33.206024Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "51"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(bond_10_yr_69_2019)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
