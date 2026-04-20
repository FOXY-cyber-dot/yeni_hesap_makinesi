import tkinter as tk
import math

class GelismisHesapMakinesi:
    def __init__(self, root):
        self.root = root
        self.root.title("Gelişmiş Python Hesap Makinesi")
        self.root.geometry("500x650")
        self.root.configure(bg="#1E1E1E")
        
        self.tum_ifade = ""
        self.mevcut_ifade = ""
        self.hesaplandi = False
        self.bellek = 0
        self.mode = "normal"
        
        self.PI = math.pi
        self.E = math.e
        
        self.arayuz_olustur()
    
    def arayuz_olustur(self):
        # Ekran
        ekran_frame = tk.Frame(self.root, bg="#252525", height=100)
        ekran_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.tum_ifade_label = tk.Label(
            ekran_frame,
            text="",
            font=("Consolas", 12),
            bg="#252525",
            fg="#A0A0A0",
            anchor="e"
        )
        self.tum_ifade_label.pack(fill=tk.X, padx=20, pady=(20, 5))
        
        self.mevcut_label = tk.Label(
            ekran_frame,
            text="0",
            font=("Consolas", 24, "bold"),
            bg="#252525",
            fg="#FFFFFF",
            anchor="e"
        )
        self.mevcut_label.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Mod seçimi
        mod_frame = tk.Frame(self.root, bg="#2D2D2D")
        mod_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Button(mod_frame, text="Normal", command=lambda: self.mod_degistir("normal"), 
                 bg="#4ECDC4", fg="white", relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
        tk.Button(mod_frame, text="Bilimsel", command=lambda: self.mod_degistir("bilimsel"), 
                 bg="#FF9F43", fg="white", relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
        tk.Button(mod_frame, text="Programcı", command=lambda: self.mod_degistir("programci"), 
                 bg="#A29BFE", fg="white", relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
        
        # Ana butonlar
        self.buton_frame = tk.Frame(self.root, bg="#1E1E1E")
        self.buton_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        self.normal_butonlari_olustur()
    
    def normal_butonlari_olustur(self):
        # Temizleme
        for widget in self.buton_frame.winfo_children():
            widget.destroy()
        
        # Normal mod butonları
        normal_butonlar = [
            ('C', '#FF6B6B'), ('⌫', '#95A5A6'), ('%', '#95A5A6'), ('÷', '#4ECDC4'), ('√', '#4ECDC4'),
            ('sin', '#FF9F43'), ('cos', '#FF9F43'), ('tan', '#FF9F43'), ('π', '#54A0FF'), ('x²', '#54A0FF'),
            ('7', '#2D3436'), ('8', '#2D3436'), ('9', '#2D3436'), ('×', '#4ECDC4'), ('1/x', '#4ECDC4'),
            ('4', '#2D3436'), ('5', '#2D3436'), ('6', '#2D3436'), ('-', '#4ECDC4'), ('log', '#FF9F43'),
            ('1', '#2D3436'), ('2', '#2D3436'), ('3', '#2D3436'), ('+', '#4ECDC4'), ('ln', '#FF9F43'),
            ('0', '#2D3436'), ('.', '#2D3436'), ('=', '#2ECC71'), ('(', '#54A0FF'), (')', '#54A0FF')
        ]
        
        for i, (text, color) in enumerate(normal_butonlar):
            row = i // 5
            col = i % 5
            
            btn = tk.Button(
                self.buton_frame,
                text=text,
                font=("Consolas", 14),
                bg=color,
                fg="white",
                activebackground="#636E72",
                relief=tk.FLAT,
                height=2,
                width=6 if text not in ['=', '0'] else 6
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            
            if text == '=':
                btn.config(command=self.hesapla)
            elif text == 'C':
                btn.config(command=self.temizle)
            elif text == '⌫':
                btn.config(command=self.sil)
            elif text in ['sin', 'cos', 'tan', '√', 'log', 'ln', 'π', 'x²', '1/x']:
                btn.config(command=lambda t=text: self.ozel_islem(t))
            else:
                btn.config(command=lambda t=text: self.buton_tikla(t))
        
        # Grid yapılandırması
        for i in range(6):
            self.buton_frame.rowconfigure(i, weight=1)
        for i in range(5):
            self.buton_frame.columnconfigure(i, weight=1)
    
    def bilimsel_butonlari_olustur(self):
        # Temizleme
        for widget in self.buton_frame.winfo_children():
            widget.destroy()
        
        # Bilimsel mod butonları
        bilimsel_butonlar = [
            ('sin⁻¹', '#FF9F43'), ('cos⁻¹', '#FF9F43'), ('tan⁻¹', '#FF9F43'), ('eˣ', '#4ECDC4'), ('10ˣ', '#4ECDC4'),
            ('sinh', '#A29BFE'), ('cosh', '#A29BFE'), ('tanh', '#A29BFE'), ('n!', '#54A0FF'), ('|x|', '#54A0FF'),
            ('C', '#FF6B6B'), ('⌫', '#95A5A6'), ('%', '#95A5A6'), ('÷', '#4ECDC4'), ('√', '#4ECDC4'),
            ('sin', '#FF9F43'), ('cos', '#FF9F43'), ('tan', '#FF9F43'), ('π', '#54A0FF'), ('e', '#54A0FF'),
            ('7', '#2D3436'), ('8', '#2D3436'), ('9', '#2D3436'), ('×', '#4ECDC4'), ('xʸ', '#4ECDC4'),
            ('4', '#2D3436'), ('5', '#2D3436'), ('6', '#2D3436'), ('-', '#4ECDC4'), ('log', '#FF9F43'),
            ('1', '#2D3436'), ('2', '#2D3436'), ('3', '#2D3436'), ('+', '#4ECDC4'), ('ln', '#FF9F43'),
            ('0', '#2D3436'), ('.', '#2D3436'), ('=', '#2ECC71'), ('(', '#54A0FF'), (')', '#54A0FF')
        ]
        
        for i, (text, color) in enumerate(bilimsel_butonlar):
            row = i // 5
            col = i % 5
            
            btn = tk.Button(
                self.buton_frame,
                text=text,
                font=("Consolas", 12),
                bg=color,
                fg="white",
                activebackground="#636E72",
                relief=tk.FLAT,
                height=2,
                width=6
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            
            if text == '=':
                btn.config(command=self.hesapla)
            elif text == 'C':
                btn.config(command=self.temizle)
            elif text == '⌫':
                btn.config(command=self.sil)
            elif text in ['sin', 'cos', 'tan', '√', 'log', 'ln', 'π', 'e', 'x²', '1/x',
                         'sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'eˣ', '10ˣ', 'sinh', 'cosh', 'tanh', 'n!', '|x|', 'xʸ']:
                btn.config(command=lambda t=text: self.bilimsel_islem(t))
            else:
                btn.config(command=lambda t=text: self.buton_tikla(t))
        
        # Grid yapılandırması
        for i in range(8):
            self.buton_frame.rowconfigure(i, weight=1)
        for i in range(5):
            self.buton_frame.columnconfigure(i, weight=1)
    
    def programci_butonlari_olustur(self):
        # Temizleme
        for widget in self.buton_frame.winfo_children():
            widget.destroy()
        
        # Programcı modu butonları
        programci_butonlar = [
            ('BIN', '#FF9F43'), ('OCT', '#FF9F43'), ('DEC', '#FF9F43'), ('HEX', '#FF9F43'), ('&', '#4ECDC4'),
            ('|', '#4ECDC4'), ('^', '#4ECDC4'), ('~', '#4ECDC4'), ('<<', '#54A0FF'), ('>>', '#54A0FF'),
            ('C', '#FF6B6B'), ('⌫', '#95A5A6'), ('%', '#95A5A6'), ('÷', '#4ECDC4'), ('MOD', '#4ECDC4'),
            ('7', '#2D3436'), ('8', '#2D3436'), ('9', '#2D3436'), ('×', '#4ECDC4'), ('AND', '#A29BFE'),
            ('4', '#2D3436'), ('5', '#2D3436'), ('6', '#2D3436'), ('-', '#4ECDC4'), ('OR', '#A29BFE'),
            ('1', '#2D3436'), ('2', '#2D3436'), ('3', '#2D3436'), ('+', '#4ECDC4'), ('XOR', '#A29BFE'),
            ('0', '#2D3436'), ('.', '#2D3436'), ('=', '#2ECC71'), ('(', '#54A0FF'), (')', '#54A0FF')
        ]
        
        for i, (text, color) in enumerate(programci_butonlar):
            row = i // 5
            col = i % 5
            
            btn = tk.Button(
                self.buton_frame,
                text=text,
                font=("Consolas", 12),
                bg=color,
                fg="white",
                activebackground="#636E72",
                relief=tk.FLAT,
                height=2,
                width=6
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            
            if text == '=':
                btn.config(command=self.hesapla)
            elif text == 'C':
                btn.config(command=self.temizle)
            elif text == '⌫':
                btn.config(command=self.sil)
            elif text in ['BIN', 'OCT', 'DEC', 'HEX', '&', '|', '^', '~', '<<', '>>', 'MOD', 'AND', 'OR', 'XOR']:
                btn.config(command=lambda t=text: self.programci_islem(t))
            else:
                btn.config(command=lambda t=text: self.buton_tikla(t))
        
        # Grid yapılandırması
        for i in range(8):
            self.buton_frame.rowconfigure(i, weight=1)
        for i in range(5):
            self.buton_frame.columnconfigure(i, weight=1)
    
    def mod_degistir(self, mod):
        self.mode = mod
        if mod == "normal":
            self.normal_butonlari_olustur()
        elif mod == "bilimsel":
            self.bilimsel_butonlari_olustur()
        elif mod == "programci":
            self.programci_butonlari_olustur()
    
    def buton_tikla(self, deger):
        if self.hesaplandi:
            self.temizle()
        
        if deger == '÷':
            self.mevcut_ifade += '/'
            self.tum_ifade += '/'
        elif deger == '×':
            self.mevcut_ifade += '*'
            self.tum_ifade += '*'
        else:
            self.mevcut_ifade += str(deger)
            self.tum_ifade += str(deger)
        
        self.guncelle()
    
    def ozel_islem(self, islem):
        try:
            if self.mevcut_ifade:
                sayi = float(self.mevcut_ifade)
                
                if islem == 'sin':
                    sonuc = math.sin(math.radians(sayi))
                elif islem == 'cos':
                    sonuc = math.cos(math.radians(sayi))
                elif islem == 'tan':
                    sonuc = math.tan(math.radians(sayi))
                elif islem == '√':
                    sonuc = math.sqrt(sayi)
                elif islem == 'log':
                    sonuc = math.log10(sayi)
                elif islem == 'ln':
                    sonuc = math.log(sayi)
                elif islem == 'π':
                    sonuc = self.PI
                elif islem == 'x²':
                    sonuc = sayi ** 2
                elif islem == '1/x':
                    sonuc = 1 / sayi
                else:
                    sonuc = sayi
                
                self.mevcut_ifade = str(round(sonuc, 10) if isinstance(sonuc, float) else sonuc)
                self.tum_ifade = f"{islem}({sayi})"
                self.hesaplandi = True
                self.guncelle()
        except:
            self.mevcut_ifade = "Hata!"
            self.guncelle()
    
    def bilimsel_islem(self, islem):
        try:
            if self.mevcut_ifade:
                sayi = float(self.mevcut_ifade)
                
                if islem == 'sin⁻¹':
                    sonuc = math.degrees(math.asin(sayi))
                elif islem == 'cos⁻¹':
                    sonuc = math.degrees(math.acos(sayi))
                elif islem == 'tan⁻¹':
                    sonuc = math.degrees(math.atan(sayi))
                elif islem == 'eˣ':
                    sonuc = math.exp(sayi)
                elif islem == '10ˣ':
                    sonuc = 10 ** sayi
                elif islem == 'sinh':
                    sonuc = math.sinh(sayi)
                elif islem == 'cosh':
                    sonuc = math.cosh(sayi)
                elif islem == 'tanh':
                    sonuc = math.tanh(sayi)
                elif islem == 'n!':
                    sonuc = math.factorial(int(sayi))
                elif islem == '|x|':
                    sonuc = abs(sayi)
                elif islem == 'xʸ':
                    self.tum_ifade += '^'
                    self.guncelle()
                    return
                elif islem == 'e':
                    sonuc = self.E
                else:
                    sonuc = sayi
                
                self.mevcut_ifade = str(round(sonuc, 10) if isinstance(sonuc, float) else sonuc)
                self.tum_ifade = f"{islem}({sayi})"
                self.hesaplandi = True
                self.guncelle()
        except:
            self.mevcut_ifade = "Hata!"
            self.guncelle()
    
    def programci_islem(self, islem):
        try:
            if self.mevcut_ifade:
                sayi = int(float(self.mevcut_ifade))
                
                if islem == 'BIN':
                    sonuc = bin(sayi)[2:]
                elif islem == 'OCT':
                    sonuc = oct(sayi)[2:]
                elif islem == 'DEC':
                    sonuc = str(sayi)
                elif islem == 'HEX':
                    sonuc = hex(sayi)[2:].upper()
                elif islem == '&':
                    self.tum_ifade += ' & '
                    self.guncelle()
                    return
                elif islem == '|':
                    self.tum_ifade += ' | '
                    self.guncelle()
                    return
                elif islem == '^':
                    self.tum_ifade += ' ^ '
                    self.guncelle()
                    return
                elif islem == '~':
                    sonuc = ~sayi
                elif islem == '<<':
                    self.tum_ifade += ' << '
                    self.guncelle()
                    return
                elif islem == '>>':
                    self.tum_ifade += ' >> '
                    self.guncelle()
                    return
                elif islem == 'MOD':
                    self.tum_ifade += ' % '
                    self.guncelle()
                    return
                elif islem == 'AND':
                    sonuc = sayi & int(self.mevcut_ifade)
                elif islem == 'OR':
                    sonuc = sayi | int(self.mevcut_ifade)
                elif islem == 'XOR':
                    sonuc = sayi ^ int(self.mevcut_ifade)
                else:
                    sonuc = sayi
                
                self.mevcut_ifade = str(sonuc)
                self.tum_ifade = f"{islem}({sayi})"
                self.hesaplandi = True
                self.guncelle()
        except:
            self.mevcut_ifade = "Hata!"
            self.guncelle()
    
    def temizle(self):
        self.tum_ifade = ""
        self.mevcut_ifade = ""
        self.hesaplandi = False
        self.guncelle()
    
    def sil(self):
        if self.mevcut_ifade:
            self.mevcut_ifade = self.mevcut_ifade[:-1]
            self.tum_ifade = self.tum_ifade[:-1]
            self.guncelle()
    
    def guncelle(self):
        self.mevcut_label.config(text=self.mevcut_ifade if self.mevcut_ifade else "0")
        self.tum_ifade_label.config(text=self.tum_ifade)
    
    def hesapla(self):
        try:
            iface = self.tum_ifade.replace('÷', '/').replace('×', '*')
            sonuc = eval(iface, {"__builtins__": None}, {"math": math})
            
            if isinstance(sonuc, float):
                if sonuc.is_integer():
                    sonuc = int(sonuc)
                else:
                    sonuc = round(sonuc, 10)
            
            self.mevcut_ifade = str(sonuc)
            self.tum_ifade = str(sonuc)
            self.hesaplandi = True
            self.guncelle()
        except ZeroDivisionError:
            self.mevcut_ifade = "Sıfıra bölme!"
            self.guncelle()
        except:
            self.mevcut_ifade = "Hata!"
            self.guncelle()

if __name__ == "__main__":
    root = tk.Tk()
    app = GelismisHesapMakinesi(root)
    root.mainloop()
