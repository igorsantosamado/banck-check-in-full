"""
Cheque por Extenso

Este problema foi utilizado em 1111 Dojo(s).

Apesar de o volume de cheques emitidos tenha diminuído drásticamente nos últimos anos, principalmente devido a
popularização dos cartões de crédito e débito, eles ainda são utilizados em muitas compras, especialmente a de valores
altos. E para auxiliar no seu preenchimento, vários estabelecimentos possuem máquinas que dado o valor da compra,
preenchem o cheque com o seu valor por extenso.

Desenvolva um programa que dado um valor monetário, seja retornado o valor em reais por extenso.

Exemplo:

    15415,16 -> quinze mil quatrocentos e quinze reais e dezesseis centavos
    0,05 -> cinco centavos
    2,25 -> dois reais e vinte e cinco centavos

"""

from num2words import num2words


def bank_check(num):
    return num2words(num, lang="pt_BR", to="currency")


if __name__ == '__main__':
    assert bank_check(15415.16) == "quinze mil, quatrocentos e quinze reais e dezesseis centavos"
    assert bank_check(0.05) == "zero reais e cinco centavos"
    assert bank_check(2.25) == "dois reais e vinte e cinco centavos"
    assert bank_check(500) == "quinhentos reais"
