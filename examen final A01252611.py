{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP66kDvwlhUn4/2JDhjK1DR",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/eliassalazarb/FisicaComputacional1/blob/main/examen%20final%20A01252611.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UOyrwT702Gzb",
        "outputId": "fc58f45e-8d5b-4ecb-b38e-680a5b74eacd"
      },
      "source": [
        "#Lorenzo Ibarra Luebbert\n",
        "#A01252611\n",
        "import random #Libreria para azar\n",
        "\n",
        "def funcion1():\n",
        "    numeros = []\n",
        "    f = open(\"numeros.txt\",\"w\")\n",
        "    for n in range(100):\n",
        "        numeros.append(str(random.randrange(1,1000)))\n",
        "    for numero in numeros:\n",
        "        f.write(\"%s\\n\" % numero)\n",
        "    f.close()\n",
        "\n",
        "def funcion2():\n",
        "    f = open(\"numeros.txt\",\"r\")\n",
        "    numeros = f.read()\n",
        "    print(numeros)\n",
        "    f.close()\n",
        "    \n",
        "def funcion3():\n",
        "    f = open(\"numeros.txt\",\"r\")\n",
        "    numeros = f.read().split('\\n')\n",
        "    numeros_int = []\n",
        "    for numero in numeros:\n",
        "        try:\n",
        "            numeros_int.append(int(numero))\n",
        "        except:\n",
        "            pass\n",
        "    print(\"Mayor: \",max(numeros_int),\"Menor: \",min(numeros_int))\n",
        "\n",
        "def funcion4():\n",
        "    f = open(\"numeros.txt\",\"r\")\n",
        "    numeros = f.read().split('\\n')\n",
        "    pares = 0\n",
        "    impares = 0\n",
        "    for numero in numeros:\n",
        "        try:\n",
        "            numero = int(numero)\n",
        "            if numero % 2 == 0:\n",
        "                pares = pares+1\n",
        "            else:\n",
        "                impares = impares + 1\n",
        "        except:\n",
        "            pass\n",
        "    f.close()\n",
        "    print(\"Pares: \",pares,\"Impares: \",impares)\n",
        "\n",
        "opcion = 0\n",
        "while opcion != 5:\n",
        "    print(\"1) Hacer archivo\")\n",
        "    print(\"2) Leer e imprimir\")\n",
        "    print(\"3) Imprimir valor mayor y menor\")\n",
        "    print(\"4) Imprimir pares y nones\")\n",
        "    print(\"5) Terminar\")\n",
        "    opcion = int(input(\"\"))\n",
        "    if opcion == 1:\n",
        "        funcion1()\n",
        "    elif opcion == 2:\n",
        "        funcion2()\n",
        "    elif opcion == 3:\n",
        "        funcion3()\n",
        "    elif opcion == 4:\n",
        "        funcion4()"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1) Hacer archivo\n",
            "2) Leer e imprimir\n",
            "3) Imprimir valor mayor y menor\n",
            "4) Imprimir pares y nones\n",
            "5) Terminar\n",
            "1\n",
            "1) Hacer archivo\n",
            "2) Leer e imprimir\n",
            "3) Imprimir valor mayor y menor\n",
            "4) Imprimir pares y nones\n",
            "5) Terminar\n",
            "2\n",
            "43\n",
            "682\n",
            "714\n",
            "276\n",
            "943\n",
            "930\n",
            "614\n",
            "647\n",
            "9\n",
            "546\n",
            "301\n",
            "627\n",
            "876\n",
            "254\n",
            "26\n",
            "295\n",
            "518\n",
            "523\n",
            "340\n",
            "237\n",
            "595\n",
            "781\n",
            "929\n",
            "864\n",
            "442\n",
            "493\n",
            "231\n",
            "27\n",
            "312\n",
            "252\n",
            "329\n",
            "424\n",
            "73\n",
            "145\n",
            "983\n",
            "662\n",
            "547\n",
            "683\n",
            "538\n",
            "682\n",
            "30\n",
            "776\n",
            "759\n",
            "416\n",
            "850\n",
            "159\n",
            "839\n",
            "106\n",
            "813\n",
            "281\n",
            "392\n",
            "607\n",
            "778\n",
            "578\n",
            "305\n",
            "978\n",
            "149\n",
            "310\n",
            "296\n",
            "870\n",
            "786\n",
            "720\n",
            "593\n",
            "228\n",
            "306\n",
            "539\n",
            "814\n",
            "598\n",
            "267\n",
            "222\n",
            "914\n",
            "139\n",
            "10\n",
            "636\n",
            "291\n",
            "928\n",
            "56\n",
            "686\n",
            "394\n",
            "987\n",
            "84\n",
            "273\n",
            "742\n",
            "63\n",
            "411\n",
            "118\n",
            "350\n",
            "621\n",
            "292\n",
            "676\n",
            "683\n",
            "96\n",
            "299\n",
            "124\n",
            "797\n",
            "617\n",
            "985\n",
            "313\n",
            "646\n",
            "991\n",
            "\n",
            "1) Hacer archivo\n",
            "2) Leer e imprimir\n",
            "3) Imprimir valor mayor y menor\n",
            "4) Imprimir pares y nones\n",
            "5) Terminar\n",
            "3\n",
            "Mayor:  991 Menor:  9\n",
            "1) Hacer archivo\n",
            "2) Leer e imprimir\n",
            "3) Imprimir valor mayor y menor\n",
            "4) Imprimir pares y nones\n",
            "5) Terminar\n",
            "4\n",
            "Pares:  54 Impares:  46\n",
            "1) Hacer archivo\n",
            "2) Leer e imprimir\n",
            "3) Imprimir valor mayor y menor\n",
            "4) Imprimir pares y nones\n",
            "5) Terminar\n",
            "5\n"
          ]
        }
      ]
    }
  ]
}