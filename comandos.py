#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cmd

class Comandos(cmd.Cmd):
    """Interprete de comandos"""
    prompt = "Introduza un comando: "
            
    def do_comando1(self, args):
        """Ayuda del comando1"""
        print("comando1 se ha ejecutado")

    def do_comando2(self, args):
        """Ayuda del comando2"""
        print("comando2 se ha ejecutado")

    def do_salir(self, args):
        """Salir del interprete"""
        print("Hasta pronto")
        return(True)

if __name__ == '__main__':
    interprete = Comandos()
    interprete.cmdloop()
