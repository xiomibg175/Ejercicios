import tkinter as tk
from tkinter import messagebox
import math


class CalculadoraEstadisticas:
    
    def __init__(self, notas):
        self.notas = notas
        self.notas_float = []
        self._validar_y_convertir()
    
    def _validar_y_convertir(self):
        try:
            self.notas_float = [float(nota) for nota in self.notas]
        except ValueError:
            raise ValueError("Las notas deben ser números válidos")
    
    def calcular_promedio(self):
        suma_para_promedio = sum(self.notas_float[1:])
        return suma_para_promedio / len(self.notas_float)
    
    def calcular_desviacion_estandar(self, promedio):
        suma_para_desviacion = 0
        for nota in self.notas_float:
            suma_para_desviacion += (nota - promedio) ** 2
        return math.sqrt(suma_para_desviacion / len(self.notas_float))
    
    def obtener_mayor(self):
        return max(self.notas_float)
    
    def obtener_menor(self):
        return min(self.notas_float)
    
    def obtener_resultados(self):
        promedio = self.calcular_promedio()
        return {
            "promedio": promedio,
            "desviacion": self.calcular_desviacion_estandar(promedio),
            "mayor": self.obtener_mayor(),
            "menor": self.obtener_menor()
        }


class VentanaNotas:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.entries_notas = []
        self.lbl_promedio = None
        self.lbl_desviacion = None
        self.lbl_mayor = None
        self.lbl_menor = None
        
        self._configurar_ventana()
        self._crear_entradas()
        self._crear_botones()
        self._crear_etiquetas_resultados()
    
    def _configurar_ventana(self):
        self.ventana.title("Notas")
        self.ventana.iconbitmap('Calculadora.ico')
        self.ventana.geometry("280x380")
        self.ventana.resizable(False, False)
    
    def _crear_entradas(self):
        for i in range(5):
            y_pos = 20 + i * 30
            
            label = tk.Label(self.ventana, text=f"Nota {i+1}:")
            label.place(x=20, y=y_pos)
            
            entry = tk.Entry(self.ventana, width=22)
            entry.place(x=105, y=y_pos)
            self.entries_notas.append(entry)
    
    def _crear_botones(self):
        btn_calcular = tk.Button(
            self.ventana, 
            text="Calcular", 
            width=12, 
            command=self.calcular
        )
        btn_calcular.place(x=35, y=180)
        
        btn_limpiar = tk.Button(
            self.ventana, 
            text="Limpiar", 
            width=12, 
            command=self.limpiar
        )
        btn_limpiar.place(x=145, y=180)
    
    def _crear_etiquetas_resultados(self):
        self.lbl_promedio = tk.Label(self.ventana, text="Promedio =")
        self.lbl_promedio.place(x=20, y=220)
        
        self.lbl_desviacion = tk.Label(self.ventana, text="Desviación estándar =")
        self.lbl_desviacion.place(x=20, y=250)
        
        self.lbl_mayor = tk.Label(self.ventana, text="Valor mayor =")
        self.lbl_mayor.place(x=20, y=280)
        
        self.lbl_menor = tk.Label(self.ventana, text="Valor menor =")
        self.lbl_menor.place(x=20, y=310)
    
    def _obtener_notas_ingresadas(self):
        return [entry.get() for entry in self.entries_notas]
    
    def _validar_entradas(self, entradas):
        if any(not entrada for entrada in entradas):
            messagebox.showerror(
                "Error de entrada", 
                "Por favor, ingrese todas las cinco notas."
            )
            return False
        return True
    
    def _mostrar_resultados(self, resultados):
        self.lbl_promedio.config(text=f"Promedio = {resultados['promedio']:.2f}")
        self.lbl_desviacion.config(text=f"Desviación estándar = {resultados['desviacion']:.2f}")
        self.lbl_mayor.config(text=f"Valor mayor = {resultados['mayor']:.1f}")
        self.lbl_menor.config(text=f"Valor menor = {resultados['menor']:.1f}")
    
    def calcular(self):
        entradas = self._obtener_notas_ingresadas()
        
        if not self._validar_entradas(entradas):
            return
        
        try:
            calculadora = CalculadoraEstadisticas(entradas)
            resultados = calculadora.obtener_resultados()
            self._mostrar_resultados(resultados)
        except ValueError:
            messagebox.showerror(
                "Error de entrada", 
                "Por favor, ingrese solo números válidos."
            )
    
    def limpiar(self):
        for entry in self.entries_notas:
            entry.delete(0, tk.END)
        
        self.lbl_promedio.config(text="Promedio =")
        self.lbl_desviacion.config(text="Desviación estándar =")
        self.lbl_mayor.config(text="Valor mayor =")
        self.lbl_menor.config(text="Valor menor =")
    
    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    app = VentanaNotas()
    app.ejecutar()