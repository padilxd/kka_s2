from abc import ABC, abstractmethod

# =============================
# Latihan 5: Abstraction / Interface
# =============================
class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


# =============================
# Latihan 1–4: Class Hero
# =============================
class Hero(GameUnit):
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.__hp = hp          # private
        self.attack_power = attack_power

    # GETTER
    def get_hp(self):
        return self.__hp

    # SETTER (validasi)
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    # Implementasi abstract method
    def info(self):
        print(f"Hero: {self.name} | HP: {self.get_hp()} | Power: {self.attack_power}")

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# =============================
# Latihan 3: Inheritance (Mage)
# =============================
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.get_hp()} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")


# =============================
# Latihan 5: Class Monster
# =============================
class Monster(GameUnit):
    def __init__(self, jenis, hp, attack_power):
        self.jenis = jenis
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Monster: {self.jenis} | HP: {self.hp} | Power: {self.attack_power}")

    def serang(self, target):
        print(f"Monster {self.jenis} menyerang {target.name}!")
        target.diserang(self.attack_power)


# =============================
# Main Program
# =============================

# Latihan 1
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.set_hp(500)
print(f"HP hero1 setelah diubah: {hero1.get_hp()}")

hero1.info()
hero2.info()

# Latihan 2
print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)
hero2.serang(hero1)

# Latihan 3
print("\n--- Mage Muncul ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)

# Latihan 4
print("\n--- Uji Enkapsulasi HP ---")
eudora.set_hp(-50)
print(f"{eudora.name} HP sekarang: {eudora.get_hp()}")

eudora.set_hp(9999)
print(f"{eudora.name} HP sekarang: {eudora.get_hp()}")

# Latihan 5
print("\n--- Hero vs Monster ---")
monster = Monster("Serigala", 150, 18)
monster.info()
monster.serang(hero1)
