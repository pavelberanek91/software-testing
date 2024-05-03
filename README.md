# Testování softwaru

## Lekce: pracovní rámec Robot

### Samostatné úkoly

#### 1. Vytvoření Testovacího projektu - Testování prototypu Receptáře

Spusťte webový projekt ve Flask z tohoto repozitáře. V prostředí Rideru vytvořte nový testovací projekt s názvem Testování prototypu Receptáře. 

#### 2. Vytvoření Testovací sady - Testy navigační lišty

Vytvořte novou testovací sadu s názvem Testy navigační lišty. Následně do ní budete vytvářet testovací případy. Testovací sadě musíte přidat testování pomocí knihovny: SeleniumLibrary.

#### 3. Vytvoření Testovacích případů pro sadu - Testy navigační lišty

Vytvořte následující testovací případy pomocí Selenia. Všechny tyto případy budou organizovány do v předešlém kroku vytvořené testovací sady.

**Testový případ NLT1**
* Je dáno: server s webovou aplikací běží a uživatel je na úvodní webové stránce.
* Když: uživatel klikně na odkaz s textem Home.
* Tak: uživatel se ocitne na stránce s koncovým bodem /home

**Testový případ NLT2**
* Je dáno: server s webovou aplikací běží a uživatel je na úvodní webové stránce.
* Když: uživatel klikně na odkaz s textem Recipes.
* Tak: uživatel se ocitne na stránce s koncovým bodem /recipes

**Testový případ NLT3**
* Je dáno: server s webovou aplikací běží a uživatel je na úvodní webové stránce.
* Když: uživatel klikně na odkaz s textem Send Us Your Recipe.
* Tak: uživatel se ocitne na stránce s koncovým bodem /form

#### 4. Vytvoření Testovací sady - Testy formuláře

Vytvořte následující novou testovací sadu s názvem Testy formuláře. Následně do ní vytvořte tyto testovací případy, které budou realizovány Seleniem.

**Testový případ FT1**
* Je dáno: server s webovou aplikací běží a uživatel je na stránce s koncovým bodem /form
* Když: uživatel zadá do vstupní položky s popiskem "Name of recipe" hodnotu "Chleba" a do vstupní položky s popiskem "Write a recipe procedure" hodnotu "Koupim ho" a odešle data kliknutím na tlačítko s textem "Send Recipe"
* Tak: uživatel se ocitne na stránce s koncovým bodem /recipes, kde uvidí v číslovaném seznamu jako poslední položku obě zadané informace.

**Testový případ FT2**
* Je dáno: server s webovou aplikací běží a uživatel je na úvodní webové stránce.
* Když: uživatel klikně na odkaz s textem Home.
* Tak: uživatel se ocitne na stránce s koncovým bodem /recipes
