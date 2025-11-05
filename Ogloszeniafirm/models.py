from django.db import models

# ===========================
# Choices / Listy wyboru
# ===========================

# Branże / główne grupy
INDUSTRY_CHOICES = [
    # --- Infrastruktura i budownictwo --- (NA POCZĄTKU!)
    ('CONSTRUCTION', 'Budownictwo / Construction'),
    ('CONSTRUCTION_FINISH', 'Prace wykończeniowe / Finishing Construction'),
    ('INFRA', 'Infra / Kabel / Telekomunikacja'),
    ('ROAD_ENGINEERING', 'Drogi i inżynieryjno-instalacyjna / Road & Engineering'),
    ('ARCHITECTURE_RENOVATION', 'Renowacja elementów architektury / Architecture Renovation'),
    ('ASSEMBLY_INSTALLATION', 'Montaże / Assembly & Installation'),
    
    # --- Przemysł i produkcja ---
    ('PRODUCTION', 'Produkcja / Production'),
    ('WELDING_METAL', 'Spawalnictwo i metalurgia / Welding & Metalwork'),
    ('METALLURGY_CASTING', 'Hutnictwo i odlewnictwo / Metallurgy & Casting'),
    ('MECHANICAL', 'Mechanika i budowa maszyn / Mechanical & Machinery'),
    ('PRECISION_MECHANICAL', 'Mechanika precyzyjna / Precision Mechanics'),
    ('CHEMICAL', 'Przemysł chemiczny / Chemical Industry'),
    ('WOOD_FURNITURE', 'Przemysł drzewny i meblarski / Wood & Furniture Industry'),
    ('SHIPYARD', 'Przemysł jachtowy i okrętowy / Shipbuilding & Yacht Industry'),
    ('AEROSPACE', 'Przemysł lotniczy / Aerospace Industry'),
    ('FOOD_PROCESSING', 'Przetwórstwo mięsa i mleka / Food Processing'),
    ('PETROCHEMICAL', 'Petrochemia, oil & gas / Petrochemical & Oil & Gas'),
    
    # --- Energetyka i elektryka ---
    ('ELECTRICAL_ELECTRONIC', 'Elektryczno-elektroniczna i energetyczna / Electrical, Electronic & Energy'),
    ('IT_TELEINFORMATICS', 'Teleinformatyczna / IT & Teleinformatics'),
    ('SOFTWARE_DEVELOPMENT', 'Programiści / Software Development'),
    ('AUTOMOTIVE', 'Motoryzacja / Automotive'),
    ('MINING_DRILLING', 'Górnictwo i wiertnictwo / Mining & Drilling'),
    
    # --- Logistyka, transport i handel ---
    ('TRANSPORT_LOGISTICS', 'Transportowo-spedycyjno-logistyczna / Transport & Logistics'),
    ('TRADE', 'Handel / Trade'),
    
    # --- Rolnictwo i środowisko ---
    ('FORESTRY_GARDENING', 'Leśno-ogrodnicza / Forestry & Gardening'),
    ('AGRICULTURE_LIVESTOCK', 'Rolno-hodowlana / Agriculture & Livestock'),
    ('FISHING', 'Rybacka / Fishing Industry'),
    
    # --- Usługi, HR i biuro ---
    ('ECONOMY_ADMINISTRATION', 'Ekonomiczno-administracyjna / Economy & Administration'),
    ('OFFICE', 'Biurowa / Office Work'),
    ('HR', 'Doradztwo HR / HR Consulting'),
    ('TRANSLATION', 'Tłumacze / Translators'),
    ('ADVERTISING', 'Reklama / Advertising'),
    ('FASHION_CREATIVE', 'Przemysł mody / Fashion & Creative Industry'),
    
    # --- Zdrowie, edukacja, turystyka ---
    ('HEALTHCARE', 'Ochrona zdrowia / Healthcare'),
    ('TOURISME', 'Hotelarstwo, gastronomia i turystyka / Hospitality & Tourism'),
    
    # --- Inne ---
    ('OTHER', 'Inne branże / Other'),
]

# Zawody w podgrupach
JOB_ROLE_CHOICES = [
    # --- Construction & Finishing (NA POCZĄTKU!) ---
    ('BRICKLAYER', 'Bricklayer / Metselaar / Maurer / Murarz / Zedník / Зидар / Murár'),
    ('BRICKLAYER_YTONG', 'Bricklayer (Ytong, Silicate, Porotherm) / Metselaar (Ytong, Silicaat, Porotherm) / Maurer (Ytong, Silikat, Porotherm) / Murarz klejony (Ytong, Silikat, Porotherm) / Zedník (Ytong, Silikát, Porotherm) / Зидар (Ytong, Силикат, Porotherm) / Murár (Ytong, Silikát, Porotherm)'),
    ('BRICKLAYER_CLINKER', 'Clinker Bricklayer / Klinkermetselaar / Klinkermaurer / Murarz klinkier / Zedník klinker / Зидар клинкер / Murár klinker'),
    ('PLASTERER', 'Plasterer / Stukadoor / Verputzer / Tynkarz / Sádrokartonář / Мазач / Sadrokartonár'),
    ('STUCCO_WORKER', 'Stucco Worker / Stucadoor / Stuckateur / Sztukator / Štukatér / Щукатор / Štukatér'),
    ('PAINTER_GENERAL', 'Painter (General Construction) / Schilder (Algemeen) / Maler / Malarz ogólnobudowlany / Malíř / Бояджия / Maliar'),
    ('PAINTER_INDUSTRIAL', 'Industrial Painter / Industrieel Schilder / Industrielackierer / Malarz przemysłowy / Průmyslový malíř / Промишлен бояджия / Priemyselný maliar'),
    ('ROOFER', 'Roofer / Dakdekker / Dachdecker / Dekarz / Pokrývač / Покривар / Pokrývač'),
    ('CARPENTER', 'Carpenter / Timmerman / Zimmerer / Stolarz / Tesař / Дърводелец / Tesár'),
    ('WINDOW_FITTER', 'Window Fitter / Ramenmonteur / Fensterbauer / Monter okien / Montér oken / Монтажник на прозорци / Montér okien'),
    ('GLASS_INSTALLER', 'Glass Installer / Glaszetter / Glaser / Monter szkła / Montér skel / Стъклар / Montér skla'),
    ('FACADE_FITTER', 'Facade Fitter / Gevelmonteur / Fassadenmonteur / Monter fasad / Montér fasád / Монтажник фасади / Montér fasád'),
    ('INDUSTRIAL_INSTALLER', 'Industrial Installer / Industrieel Monteur / Industriemonteur / Monter przemysłowy / Priemyselný montér / Индустриален монтажник / Priemyselný montér'),
    ('INSULATION_FITTER', 'Insulation Fitter / Isolatiemonteur / Isolierer / Monter izolacji / Izolatér / Монтажник изолации / Izolatér'),
    ('SCAFFOLDER', 'Scaffolder / Steigerbouwer / Gerüstbauer / Monter rusztowań / Lešenář / Монтажник на скелета / Lešenár'),
    ('SCAFFOLDER_ASSISTANT', 'Scaffolder Assistant / Assistent Steigerbouwer / Gerüstbauhelfer / Pomocnik montera rusztowań / Pomocník lešenáře / Помощник на монтажник скеле / Pomocník lešenára'),
    ('GENERAL_WORKER', 'General Construction Worker / Bouwvakker / Bauarbeiter / Pracownik ogólnobudowlany / Dělník stavební / Строителен работник / Stavebný robotník'),
    ('PLUMBER', 'Plumber / Loodgieter / Installateur / Hydraulik / Instalater / Водопроводчик / Inštalatér'),
    ('ELECTRICIAN', 'Electrician / Elektricien / Elektriker / Elektryk / Elektrikář / Електротехник / Elektrikár'),
    ('ELECTROTECHNICIAN', 'Electrotechnician / Elektrotechnicus / Elektrotechniker / Elektrotechnik / Elektrotechnik / Електротехник / Elektrotechnik'),
    ('FOREMAN', 'Construction Foreman / Voorman Bouw / Bauleiter / Brygadzista budowlany / Stavbyvedoucí / Бригадир / Stavbyvedúci'),
    ('ENGINEER_CONSTRUCTION', 'Construction Engineer / Bouwkundig Ingenieur / Bauingenieur / Inżynier budownictwa / Stavební inženýr / Строителен инженер / Stavebný inžinier'),
    ('SURVEYOR', 'Surveyor / Landmeter / Vermessungsingenieur / Geodeta / Zeměměřič / Геодезист / Geodet'),
    ('ARCHITECT', 'Architect / Architect / Architekt / Architekt / Architekt / Архитект / Architekt'),

    # --- Pomocnicy / Asystenci ---
    ('HELPER_WINDOW_INSTALLER', 'Pomocnik montera okien / Hulpmonteur ramen / Helfer Fenster / Pomocnik montera okien / Pomocnik montażu oken / Помощник монтажника окон'),
    ('HELPER_FACADE_INSTALLER', 'Pomocnik montera fasad / Hulpmonteur gevels / Helfer Fassade / Pomocnik montera fasad / Pomocnik montażu fasad / Помощник монтажника фасадов'),
    ('HELPER_CONSTRUCTION', 'Pomocnik montera budowlanego / Hulpmonteur bouw / Helfer Bau / Pomocnik montera budowlanego / Pomocnik montażu budowlanego / Помощник монтажника строительства'),
    ('SCAFFOLDING_HELPER', 'Pomocnik montera rusztowań / Hulpmonteur steigers / Helfer Gerüst / Pomocnik montera rusztowań / Pomocnik montażysty rusztowań / Помощник монтажника лесов'),
    
    # --- Infra / Kabel / Telekom ---
    ('CABLE_INSTALLER', 'Cable Installer / Kabelmonteur / Monter kabli / Instalatér kabelů / Монтажник кабели / Montér káblov / Монтажник кабелів'),
    ('NETWORK_CABLER', 'Network Cabler / Netwerkkabelaar / Kabelarz sieciowy / Síťový kabelář / Мрежов кабелист / Sieťový kabelár / Мережевий кабелист'),
    ('FIBER_INSTALLER', 'Fiber Optic Installer / Glasvezelmonteur / Monter światłowodów / Montér optických vláken / Монтажник оптични влакна / Montér optických vlákien / Монтажник оптоволокна'),

    # --- Mechanical ---
    ('MECHANIC_GENERAL', 'Mechanic / Monteur / Mechaniker / Mechanik / Mechanik / Механик / Mechanik'),
    ('INDUSTRIAL_MECHANIC', 'Industrial Mechanic / Industrieel Monteur / Industriemechaniker / Mechanik maszyn przemysłowych / Průmyslový mechanik / Промишлен механик / Priemyselný mechanik'),
    ('LOCKSMITH', 'Locksmith / Slotenmaker / Schlosser / Ślusarz / Zámečník / Шлосер / Zámočník'),
    ('CNC_OPERATOR', 'CNC Machine Operator / CNC-Operator / CNC-Maschinenbediener / Operator CNC / Operátor CNC / Оператор на CNC / Operátor CNC'),
    ('CNC_PROGRAMMER', 'CNC Programmer / CNC-Programmeur / CNC-Programmierer / Programista CNC / Programátor CNC / Програмист CNC / Programátor CNC'),
    ('MACHINE_FITTER', 'Machine Fitter / Machine Monteur / Maschinenmonteur / Monter maszyn / Montér strojů / Монтажник машини / Montér strojov'),
    ('MECHANICAL_FITTER', 'Mechanical Fitter / Mechanisch Monteur / Mechanischer Monteur / Monter mechaniczny / Mechanický montér / Механичен монтажник / Mechanický montér'),
    ('MAINTENANCE_TECHNICIAN', 'Maintenance Technician / Onderhoudstechnicus / Instandhaltungstechniker / Technik utrzymania ruchu / Technik údržby / Техник поддръжка / Technik údržby'),
    ('MACHINE_OPERATOR', 'Machine Operator / Machinebediener / Maschinenführer / Operator maszyn / Operátor strojů / Оператор машини / Operátor strojov'),
    ('MACHINE_ASSEMBLER', 'Machine Assembler / Machine Monteur / Maschinenbauer / Monter maszyn przemysłowych / Montér priemyselných strojov / Монтажник промишлени машини / Montér priemyselných strojov'),
    ('TOOLMAKER', 'Toolmaker / Gereedschapsmaker / Werkzeugmacher / Narzędziowiec / Nástrojař / Инструменталчик / Nástrojár'),
    ('METALWORKER', 'Metalworker / Metaalbewerker / Metallbearbeiter / Metalowiec / Kovodělník / Металообработчик / Kovospracovateľ'),
    ('TURNER', 'Turner / Draaier / Dreher / Tokarz / Soustružník / Стругар / Sústružník'),
    ('MILLER', 'Miller / Frezer / Fräser / Frezer / Frézař / Фрезист / Frézar'),
    ('HYDRAULIC_MECHANIC', 'Hydraulic Mechanic / Hydraulisch Monteur / Hydraulikmechaniker / Mechanik hydrauliki / Hydraulický mechanik / Хидравличен механик / Hydraulický mechanik'),
    ('PNEUMATIC_MECHANIC', 'Pneumatic Mechanic / Pneumatisch Monteur / Pneumatikmechaniker / Mechanik pneumatyki / Pneumatický mechanik / Пневматичен механик / Pneumatický mechanik'),

    # --- Precision Mechanical ---
    ('PRECISION_MECHANIC', 'Precision Mechanic / Precisie Mechanicus / Präzisionsmechaniker / Mechanik precyzyjny / Přesný mechanik / Прецизен механик / Presný mechanik / Прецизійний механік'),
    ('WATCHMAKER', 'Watchmaker / Klokkenmaker / Uhrmacher / Zegarmistrz / Hodinář / Часовникар / Hodinár / Годинникар'),

    # --- Electrical ---
    ('ELECTRICIAN_GENERAL', 'Electrician / Elektricien / Elektriker / Elektryk / Elektrikář / Електротехник / Elektrikár'),
    ('INDUSTRIAL_ELECTRICIAN', 'Industrial Electrician / Industrieel Elektricien / Industrieelektriker / Elektryk przemysłowy / Průmyslový elektrikář / Промишлен електротехник / Priemyselný elektrikár'),
    ('AUTOMATION_ELECTRICIAN', 'Automation Electrician / Automatiseringselektricien / Automatisierungselektriker / Elektryk automatyk / Automatizační elektrikář / Електротехник автоматизация / Automatizačný elektrikár'),
    ('ELECTRICAL_MAINTENANCE_TECH', 'Electrical Maintenance Technician / Technicus elektrisch onderhoud / Elektrotechniker Wartung / Technik utrzymania elektryki / Technik údržby elektrických zařízení / Техник поддръжка електро / Technik údržby elektrických zariadení'),
    ('HIGH_VOLTAGE_ELECTRICIAN', 'High Voltage Electrician / Hoogspanningsmonteur / Hochspannungs-Elektriker / Elektryk wysokiego napięcia / Vysokonapěťový elektrikář / Високо напрежение електротехник / Vysokonapätový elektrikár'),
    ('ELECTRICAL_ENGINEER_ASSISTANT', 'Electrical Engineer Assistant / Assistent Elektrotechnisch Ingenieur / Assistent Elektrotechniker / Asystent inżyniera elektryka / Asistent elektroinženýra / Асистент електроинженер / Asistent elektrotechnika'),
    ('SOLAR_ELECTRICIAN', 'Solar Electrician / Zonnepaneel elektricien / Solarelektriker / Elektryk fotowoltaiki / Solární elektrikář / Соларен електротехник / Solárny elektrikár'),
    ('MAINTENANCE_ELECTRICIAN', 'Maintenance Electrician / Onderhoudselektricien / Wartungselektriker / Elektryk utrzymania ruchu / Údržbář elektrikář / Техник поддръжка електро / Údržbový elektrikár'),

    # --- Production ---
    ('ASSEMBLY_WORKER', 'Assembly Worker / Monteur produkcji / Produktionsmitarbeiter / Monter produkcji / Montér výroby / Производствен работник / Montér výroby'),
    ('PACKER', 'Packer / Pakowacz / Verpacker / Pakowacz / Balíčkovač / Опаковчик / Balenár'),
    ('PRODUCTION_WORKER', 'Production Worker / Pracownik produkcji / Produktionsmitarbeiter / Pracownik produkcji / Pracovník výroby / Работник производство / Výrobný pracovník'),
    ('QUALITY_CONTROLLER', 'Quality Controller / Kontroler jakości / Qualitätskontrolleur / Kontroler jakości / Kontrolor kvality / Контролер качество / Kontrolór kvality'),
    ('PRODUCTION_OPERATOR', 'Production Operator / Productieoperator / Produktionsmitarbeiter / Operator produkcji / Operátor výroby / Оператор производство / Operátor výroby'),

    # --- Chemical Industry ---
    ('CHEMICAL_OPERATOR', 'Chemical Operator / Chemisch Operator / Chemieanlagenbediener / Operator procesów chemicznych / Chemický operátor / Химически оператор / Chemický operátor / Оператор хімічного виробництва'),
    ('LAB_TECHNICIAN', 'Lab Technician / Laboratorium Technicus / Labortechniker / Technik laboratoryjny / Laborant / Лаборант / Laborant / Лаборант'),
    ('PRODUCTION_CHEMIST', 'Production Chemist / Productie Chemicus / Produktionschemiker / Chemik produkcyjny / Výrobní chemik / Производствен химик / Výrobný chemik / Виробничий хімік'),
    ('SAFETY_SPECIALIST', 'Safety Specialist / Veiligheidspecialist / Sicherheitsfachkraft / Specjalista ds. BHP / Bezpečnostní specialista / Специалист по безопасност / Bezpečnostný špecialista / Спеціаліст з безпеки'),

    # --- Wood & Furniture Industry ---
    ('CABINETMAKER', 'Cabinetmaker / Meubelmaker / Möbelschreiner / Meblarz / Truhlář / Производител на мебели / Truhlár / Мебляр'),
    ('WOOD_MACHINE_OPERATOR', 'Wood Machine Operator / Houtmachine Operator / Holzbearbeitungsmaschinen-Bediener / Operator maszyn stolarskich / Obsluha dřevoobráběcího stroje / Оператор дървообработваща машина / Obsluha drevospracovacej stroje / Оператор деревообробного верстата'),
    ('FURNITURE_ASSEMBLER', 'Furniture Assembler / Meubelmonteur / Möbelmonteur / Monter mebli / Montér nábytku / Монтажник на мебели / Montér nábytku / Монтажник меблів'),

    # --- Shipyard Industry ---
    ('SHIPBUILDER', 'Shipbuilder / Scheepsbouwer / Schiffbauer / Stoczniowiec / Stavitel lodí / Корабостроител / Staviteľ lodí / Суднобудівник'),
    ('MARINE_ELECTRICIAN', 'Marine Electrician / Maritiem Elektricien / Schiffs-Elektriker / Elektryk okrętowy / Lodní elektrikář / Морски електротехник / Lodný elektrikár / Морський електрик'),
    ('MARINE_MECHANIC', 'Marine Mechanic / Maritiem Monteur / Schiffsmechaniker / Mechanik okrętowy / Lodní mechanik / Морски механик / Lodný mechanik / Морський механік'),
    ('SHIP_WELDER', 'Welder / Lasser / Schweißer / Spawacz okrętowy / Svářeč / Зварчик / Zvárač / Суднобудівельник-спайвач'),

    # --- Aerospace Industry ---
    ('AIRCRAFT_MECHANIC', 'Aircraft Mechanic / Vliegtuigmonteur / Flugzeugmechaniker / Mechanik lotniczy / Letadlový mechanik / Авиационен механик / Letecký mechanik / Механік літаків'),
    ('AVIONICS_TECHNICIAN', 'Avionics Technician / Avionica Technicus / Avionik-Techniker / Technik awioniki / Technik avioniky / Авионен техник / Technik avioniky / Технік авіоніки'),
    ('AEROSPACE_ENGINEER', 'Aerospace Engineer / Luchtvaartingenieur / Luftfahrtingenieur / Inżynier lotnictwa / Letový inžinier / Авиоинженер / Letecký inžinier / Інженер авіації'),
    ('ASSEMBLY_TECHNICIAN', 'Assembly Technician / Montage Technicus / Montagetechniker / Monter elementów lotniczych / Montážní technik / Техник по монтажу / Montážny technik / Технік монтажу'),

    # --- Food Processing ---
    ('MEAT_PROCESSOR', 'Meat Processor / Vleesverwerker / Fleischverarbeiter / Przetwórca mięsa / Zpracovatel masa / Месар / Spracovateľ mäsa / М\'ясник'),
    ('DAIRY_WORKER', 'Dairy Worker / Zuivelmedewerker / Molkereiarbeiter / Pracownik mleczarni / Pracovník mlékárny / Млечар / Mliečny pracovník / Працівник молочної промисловості'),
    ('FOOD_QUALITY_CONTROLLER', 'Food Quality Controller / Voedselkwaliteitscontroleur / Lebensmittelkontrolleur / Kontroler jakości żywności / Kontrolor kvality potravin / Контрол на качеството на храна / Kontrolór kvality potravín / Контролер якості продуктів'),
    ('PACKAGING_OPERATOR', 'Packaging Operator / Verpakkingsoperator / Verpackungsmitarbeiter / Operator linii pakowania / Operátor balení / Оператор опаковане / Operátor balenia / Оператор пакування'),

    # --- Petrochemical & Oil/Gas ---
    ('CHEMICAL_PLANT_OPERATOR', 'Chemical Plant Operator / Chemische installatieoperator / Chemieanlagenbediener / Operator instalacji chemicznej / Operátor chemického závodu / Оператор химическа инсталация / Operátor chemického závodu / Оператор хімічного заводу'),
    ('DRILLING_TECHNICIAN', 'Drilling Technician / Boortechnicus / Bohrtechniker / Technik wiertniczy / Technik vrtání / Техник сондаж / Technológ vŕtania / Технік буріння'),
    ('SAFETY_OFFICER', 'Safety Officer / Veiligheidsfunctionaris / Sicherheitsbeauftragter / Specjalista ds. BHP / Bezpečnostní pracovník / Служител безопасност / Bezpečnostný pracovník / Спеціаліст з охорони праці'),

    # --- Transport / Logistics ---
    ('DRIVER_CE', 'Driver CE / Kierowca kat. CE (TIR) / Fahrer CE / Kierowca kat. CE (TIR) / Řidič CE / Шофьор CE / Vodič CE'),
    ('DRIVER_C', 'Driver C / Kierowca kat. C / Fahrer C / Kierowca kat. C / Řidič C / Шофьор C / Vodič C'),
    ('DRIVER_B', 'Driver B / Kierowca kat. B / dostawca / Fahrer B / Kierowca kat. B / Řidič B / Шофьор B / Vodič B'),
    ('FORKLIFT_OPERATOR', 'Forklift Operator / Operator wózka widłowego / Gabelstaplerfahrer / Operator wózka widłowego / Vysokozdvižný vozík operátor / Въже кари оператор / Vysokozdvižný vozík operátor'),
    ('WAREHOUSE_WORKER', 'Warehouse Worker / Magazynier / Lagerarbeiter / Magazynier / Skladník / Работник склад / Skladník'),
    ('LOGISTICS_COORDINATOR', 'Logistics Coordinator / Koordynator logistyki / Logistikkoordinator / Koordynator logistyki / Koordinátor logistiky / Координатор логистика / Koordinátor logistiky'),
    ('DISPATCHER', 'Dispatcher / Dyspozytor transportu / Disponent / Dyspozytor transportu / Dispečer / Диспетчер / Dispečer'),

    # --- IT / Technology / Programming ---
    ('SOFTWARE_DEVELOPER', 'Software Developer / Programista / Softwareentwickler / Programista / Vývojář softwaru / Софтуерен разработчик / Vývojár softvéru'),
    ('WEB_DEVELOPER', 'Web Developer / Frontend Developer / Webentwickler / Frontend Developer / Webový vývojář / Уеб разработчик / Webový vývojár'),
    ('BACKEND_DEVELOPER', 'Backend Developer / Backend Developer / Backend-Entwickler / Backend Developer / Backend vývojář / Бекенд разработчик / Backend vývojár'),
    ('FULLSTACK_DEVELOPER', 'Full Stack Developer / Full Stack Developer / Full-Stack-Entwickler / Full Stack Developer / Full Stack vývojář / Фул стaк разработчик / Fullstack vývojár'),
    ('SYSTEM_ADMIN', 'System Administrator / Administrator systemów / Systemadministrator / Administrator systemów / Správce systému / Системен администратор / Správca systému'),
    ('IT_SUPPORT', 'IT Support / Technik IT / Helpdesk / IT-Support / Technik IT / Podpora IT / IT podpora / IT podpora'),
    ('NETWORK_ENGINEER', 'Network Engineer / Inżynier sieciowy / Netzwerktechniker / Inżynier sieciowy / Síťový inženýr / Мрежов инженер / Sieťový inžinier'),

    # --- HR / Office / Consulting / Translation ---
    ('HR_CONSULTANT', 'HR Consultant / Doradca HR / Personalberater / Doradca HR / HR konzultant / Консултант ЧР / HR konzultant'),
    ('HR_ASSISTANT', 'HR Assistant / Asystent HR / HR-Assistent / Asystent HR / Asistent HR / Асистент ЧР / Asistent HR'),
    ('ACCOUNTANT', 'Accountant / Księgowy / Buchhalter / Księgowy / Účetní / Счетоводител / Účtovník'),
    ('OFFICE_ASSISTANT', 'Office Assistant / Asystent biurowy / Büroassistent / Asystent biurowy / Kancelářský asistent / Офис асистент / Asistent kancelárie'),
    ('ADMINISTRATOR', 'Administrator / Administrator biura / Administrator / Administrator biura / Administrátor / Администратор / Administrátor'),
    ('TRANSLATOR', 'Translator / Tłumacz / Übersetzer / Tłumacz / Překladatel / Преводач / Prekladateľ'),
    ('CONSULTANT', 'Business Consultant / Doradca biznesowy / Unternehmensberater / Doradca biznesowy / Obchodní konzultant / Бизнес консултант / Obchodný konzultant'),
    ('LAWYER', 'Lawyer / Prawnik / Rechtsanwalt / Prawnik / Právník / Адвокат / Právnik'),

    # --- Healthcare / Medical ---
    ('NURSE', 'Nurse / Pielęgniarka / Krankenschwester / Pielęgniarka / Zdravotní sestra / Медицинска сестра / Sestra'),
    ('CAREGIVER', 'Caregiver / Opiekun / Betreuer / Opiekun / Pečovatel / Домашен помощник / Opatrovateľ'),
    ('DENTAL_ASSISTANT', 'Dental Assistant / Asystentka stomatologiczna / Zahnmedizinische Assistentin / Asystentka stomatologiczna / Zubní asistent / Зъболекарски асистент / Zubný asistent'),
    ('DOCTOR', 'Doctor / Lekarz / Arzt / Lekarz / Lékař / Лекар / Lekár'),
    ('PHARMACY_TECHNICIAN', 'Pharmacy Technician / Technik farmaceutyczny / Pharmazeutisch-technischer Assistent / Technik farmaceutyczny / Farmaceutický technik / Фармацевт / Farmaceutický technik'),
]

# Kraje (dla country)
COUNTRY_CHOICES = [
    ('NL', 'Holandia / Netherlands'),
    ('PL', 'Polska / Poland'),
    ('DE', 'Niemcy / Germany'),
    ('CZ', 'Czechy / Czech Republic'),
    ('BG', 'Bułgaria / Bulgaria'),
    ('SK', 'Słowacja / Slovakia'),
    ('UA', 'Ukraina / Ukraine'),
    ('OTHER', 'Inny kraj / Other country'),
]

# Opcje pracy zdalnej
REMOTE_OPTION_CHOICES = [
    ('ONSITE', 'Na miejscu / On-site / Op locatie'),
    ('REMOTE', 'Zdalna / Remote / Op afstand'),
    ('HYBRID', 'Hybrydowa / Hybrid / Hybride'),
]

# Zakwaterowanie
ACCOMMODATION_CHOICES = [
    ('NOT_PROVIDED', 'Brak / Not provided / Niet voorzien'),
    ('PROVIDED', 'Zapewnione / Provided / Voorzien'),
    ('OWN_ACCOMMODATION', 'Zakwaterowanie własne / Own accommodation / Eigen accommodatie'),
]

# Transport
TRANSPORT_CHOICES = [
    ('NOT_PROVIDED', 'Brak / Not provided / Niet voorzien'),
    ('PROVIDED', 'Zapewniony / Provided / Voorzien'),
    ('OWN_TRANSPORT', 'Transport własny / Own transport / Eigen vervoer'),
    ('REIMBURSED', 'Zwrot kosztów / Reimbursed / Vergoeding'),
]

# Miasta w Holandii
NL_CITIES = {
    'NORTH_HOLLAND': [
        'Amsterdam', 'Haarlem', 'Almere', 'Zaanstad', 'Haarlemmermeer', 'Volendam', 
        'Castricum', 'Lelystad', 'Urk', 'Zoetermeer', 'Anders / Inny'
    ],
    'SOUTH_HOLLAND': [
        'Rotterdam', 'Den Haag', 'Dordrecht', 'Leiden', 'Goes', 'Vlissingen', 
        'Terneuzen', 'Etten-Leur', 'Boxtel', 'Helmond', 'Anders / Inny'
    ],
    'UTRECHT': [
        'Utrecht', 'Amersfoort', 'Zeist', 'Nijwegen', 'Wijchen', 'Veghel', 'Uden', 'Deurne', 'Anders / Inny'
    ],
    'NORTH_BRABANT': [
        'Breda', 'Bergen op Zoom', 'Etten-Leur', 'Helmond', 'Veghel', 'Uden', 'Boxtel', 'Deurne', 'Anders / Inny'
    ],
    'LIMBURG': [
        'Maastricht', 'Roermond', 'Venlo', 'Venray', 'Kerkrade', 'Oosterhoud', 'Anders / Inny'
    ],
    'GELDERLAND': [
        'Arnhem', "'s-Hertogenbosch", 'Nijmegen', 'Apeldoorn', 'Wijchen', 'Anders / Inny'
    ],
    'FRIESLAND': [
        'Leeuwarden', 'Boksum', 'Dokkum', 'Harlingen', 'Anders / Inny'
    ],
    'GRONINGEN': [
        'Groningen', 'Uithuizen', 'Delfzijl', 'Winschoten', 'Hoogezand', 'Meppen', 'Assen', 'Hoogeveen', 'Emmen', 'Anders / Inny'
    ],
    'OVERIJSSEL': [
        'Enschede', 'Zwolle', 'Anders / Inny'
    ],
    'ZEELAND': [
        'Goes', 'Terneuzen', 'Zierikzee', 'Vlissingen', 'Anders / Inny'
    ],
    'FLEVOLAND': [
        'Lelystad', 'Urk', 'Anders / Inny'
    ],
    'OTHER': [
        'Cappelke van de IJzel', 'Anders / Inny'
    ]
}

# Miasta w innych krajach
PL_CITIES = [
    'Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Gdańsk', 'Szczecin', 
    'Lublin', 'Katowice', 'Białystok', 'Inne miasto / Anders / Other'
]

DE_CITIES = [
    'Berlin', 'Hamburg', 'Monachium', 'Kolonia', 'Frankfurt', 'Stuttgart', 
    'Düsseldorf', 'Dortmund', 'Essen', 'Leipzig', 'Inne miasto / Anders / Other'
]

CZ_CITIES = [
    'Praga', 'Brno', 'Ostrava', 'Plzeň', 'Liberec', 'Olomouc', 'Ústí nad Labem', 
    'Hradec Králové', 'Pardubice', 'Zlín', 'Inne miasto / Anders / Other'
]

BG_CITIES = [
    'Sofia', 'Płowdiw', 'Warna', 'Burgas', 'Ruse', 'Stara Zagora', 'Pleven', 
    'Sliven', 'Dobricz', 'Szumen', 'Inne miasto / Anders / Other'
]

SK_CITIES = [
    'Bratysława', 'Koszyce', 'Preszów', 'Żylina', 'Nitra', 'Banská Bystrica', 
    'Trnava', 'Martin', 'Inne miasto / Anders / Other'
]

UA_CITIES = [
    'Kijów', 'Charków', 'Dnipro', 'Odessa', 'Lwów', 'Zaporoże', 'Donieck', 
    'Krzywy Róg', 'Mikołajów', 'Cherson', 'Inne miasto / Anders / Other'
]

# Poziom wykształcenia
EDUCATION_LEVEL_CHOICES = [
    ('PRIMARY', 'Podstawowe / Primary / Basisschool / Grundschule / Základní / Начално / Начално образование'),
    ('SECONDARY', 'Średnie / Secondary / Middelbare school / Sekundarschule / Střední / Средно / Средно образование'),
    ('VOCATIONAL', 'Zawodowe / Vocational / Beroepsonderwijs / Berufsausbildung / Odborné / Професионално / Професионално образование'),
    ('BACHELOR', 'Licencjat / Bachelor / Bachelor / Bachelor / Bakalář / Бакалавър / Bakalár'),
    ('MASTER', 'Magister / Master / Master / Master / Magister / Магистър / Magister'),
    ('DOCTORATE', 'Doktor / Doctorate / Doctor / Doktor / Doktor / Доктор / Doktor'),
    ('OTHER', 'Inne / Other / Anders / Andere / Jiné / Друго / Iné'),
]

# Poziom doświadczenia
EXPERIENCE_LEVEL_CHOICES = [
    ('NO_EXPERIENCE', 'Brak doświadczenia / No experience / Geen ervaring / Keine Erfahrung / Žádné zkušenosti / Без опит / Žiadne skúsenosti'),
    ('LESS_1_YEAR', 'Mniej niż 1 rok / Less than 1 year / Minder dan 1 jaar / Weniger als 1 Jahr / Méně než 1 rok / Под 1 година / Menej ako 1 rok'),
    ('1_2_YEARS', '1-2 lata / 1-2 years / 1-2 jaar / 1-2 Jahre / 1-2 roky / 1-2 години / 1-2 roky'),
    ('3_5_YEARS', '3-5 lat / 3-5 years / 3-5 jaar / 3-5 Jahre / 3-5 let / 3-5 години / 3-5 rokov'),
    ('5_PLUS_YEARS', 'Ponad 5 lat / Over 5 years / Meer dan 5 jaar / Mehr als 5 Jahre / Více než 5 let / Повече от 5 години / Viac než 5 rokov'),
]

# Typ zatrudnienia
EMPLOYMENT_TYPE_CHOICES = [
    ('FULL_TIME', 'Pełen etat / Full-time / Voltijd / Vollzeit / Plný úvazek / Пълен работен ден / Plný úväzok'),
    ('PART_TIME', 'Część etatu / Part-time / Deeltijd / Teilzeit / Částečný úvazek / Частичен работен ден / Čiastočný úväzok'),
    ('TEMPORARY', 'Tymczasowa / Temporary / Tijdelijk / Befristet / Dočasná / Временна / Dočasná'),
    ('INTERNSHIP', 'Praktyka / Internship / Stage / Praktikum / Stáž / Стаж / Stáž'),
    ('TRAINEE', 'Staż / Trainee / Stage / Praktikant / Stážista / Стажант / Stážista'),
    ('FREELANCE', 'Freelance / Freelance / Freelance / Freiberuflich / Freelance / Фрийланс / Freelance'),
    ('CONTRACT', 'Umowa / Contract / Contract / Vertrag / Smlouva / Договор / Zmluva'),
]

# Liczba godzin pracy w tygodniu
WEEKLY_HOURS_CHOICES = [
    ('LESS_8', 'Mniej niż 8h / Less than 8h'),
    ('H16', '16 godzin / 16h'),
    ('H24', '24 godziny / 24h'),
    ('H32', '32 godziny / 32h'),
    ('H40', '40 godzin / 40h'),
    ('PART_40', '40 godzin – część godzin / 40h – partial hours'),
]

# Nadgodziny
OVERTIME_CHOICES = [
    ('NONE', 'Brak / None'),
    ('AVAILABLE', 'Dostępne / Available'),
    ('OPTIONAL', 'Opcjonalne / Optional'),
]

# Typ wynagrodzenia
SALARY_TYPE_CHOICES = [
    ('NEGOTIABLE', 'Do uzgodnienia / Negotiable / Te bespreken'),
    ('HOURLY', 'Stawka godzinowa / Hourly rate / Uurtarief'),
    ('MONTHLY', 'Miesięczna / Monthly / Maandelijks'),
    ('ANNUAL', 'Roczna / Annual / Jaarlijks'),
]

# Języki
LANGUAGE_CHOICES = [
    ('EN', 'Angielski / English'),
    ('NL', 'Holenderski / Dutch'),
    ('DE', 'Niemiecki / German'),
    ('PL', 'Polski / Polish'),
    ('RU', 'Rosyjski / Russian'),
    ('CS', 'Czeski / Czech'),
    ('BG', 'Bułgarski / Bulgarian'),
    ('SK', 'Słowacki / Slovak'),
    ('UA', 'Ukraiński / Ukrainian'),
    ('OTHER', 'Inny / Other'),
]

# Poziom znajomości języka
LANGUAGE_LEVEL_CHOICES = [
    ('BASIC', 'Podstawowy / Basic'),
    ('INTERMEDIATE', 'Średni / Intermediate'),
    ('ADVANCED', 'Komunikatywny / Advanced'),
]

# ===========================
# Models / Modele
# ===========================

class JobPosting(models.Model):
    """Model oferty pracy / Job posting model"""
    
    title = models.CharField(
        max_length=200,
        verbose_name="Tytuł oferty / Job title"
    )
    
    company_name = models.CharField(
        max_length=200,
        verbose_name="Nazwa firmy / Company name"
    )
    
    positions_available = models.PositiveIntegerField(
        default=1,
        verbose_name="Liczba wolnych stanowisk / Positions available",
        help_text="Ile osób poszukujemy na to stanowisko"
    )
    
    industry = models.CharField(
        max_length=50,
        choices=INDUSTRY_CHOICES,
        verbose_name="Branża / Industry"
    )
    
    job_role = models.CharField(
        max_length=50,
        choices=JOB_ROLE_CHOICES,
        verbose_name="Stanowisko / Job role"
    )
    
    description = models.TextField(
        verbose_name="Opis stanowiska / Job description"
    )
    
    # NOWE POLE: Kraj
    country = models.CharField(
        max_length=50,
        choices=COUNTRY_CHOICES,
        blank=True,
        null=True,
        verbose_name="Kraj / Country"
    )
    
    location = models.CharField(
        max_length=100,
        verbose_name="Lokalizacja / Location"
    )
    
    # NOWE POLE: Opcja pracy zdalnej
    remote_option = models.CharField(
        max_length=50,
        choices=REMOTE_OPTION_CHOICES,
        blank=True,
        null=True,
        default='ONSITE',
        verbose_name="Praca zdalna / Remote option"
    )
    
    language_required = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        verbose_name="Wymagany język / Required language"
    )
    
    language_level = models.CharField(
        max_length=20,
        choices=LANGUAGE_LEVEL_CHOICES,
        verbose_name="Poziom języka / Language level"
    )
    
    weekly_hours = models.CharField(
        max_length=10,
        choices=WEEKLY_HOURS_CHOICES,
        blank=True,
        null=True,
        verbose_name="Liczba godzin w tygodniu / Weekly hours"
    )
    
    overtime = models.CharField(
        max_length=10,
        choices=OVERTIME_CHOICES,
        default='NONE',
        verbose_name="Nadgodziny / Overtime"
    )
    
    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default='FULL_TIME',
        verbose_name="Typ zatrudnienia / Employment type"
    )
    
    # NOWE POLA: Szczegółowe informacje o ofercie
    requirements = models.TextField(
        blank=True,
        null=True,
        verbose_name="Wymagania / Requirements",
        help_text="Czego oczekujemy od kandydata (doświadczenie, certyfikaty, umiejętności)"
    )
    
    responsibilities = models.TextField(
        blank=True,
        null=True,
        verbose_name="Obowiązki / Responsibilities",
        help_text="Co będzie robił pracownik na tym stanowisku"
    )
    
    benefits = models.TextField(
        blank=True,
        null=True,
        verbose_name="Oferujemy / We offer",
        help_text="Wynagrodzenie, benefity, warunki pracy, możliwości rozwoju"
    )
    
    salary_type = models.CharField(
        max_length=20,
        choices=SALARY_TYPE_CHOICES,
        default='NEGOTIABLE',
        verbose_name="Typ wynagrodzenia / Salary type"
    )
    
    salary_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Wynagrodzenie od / Salary from",
        help_text="Minimalna kwota (w EUR)"
    )
    
    salary_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Wynagrodzenie do / Salary to",
        help_text="Maksymalna kwota (w EUR)"
    )
    
    salary_currency = models.CharField(
        max_length=3,
        default='EUR',
        verbose_name="Waluta / Currency",
        help_text="EUR, PLN, USD, itp."
    )
    
    accommodation = models.CharField(
        max_length=20,
        choices=ACCOMMODATION_CHOICES,
        default='NOT_PROVIDED',
        verbose_name="Zakwaterowanie / Accommodation"
    )
    
    transport = models.CharField(
        max_length=20,
        choices=TRANSPORT_CHOICES,
        default='NOT_PROVIDED',
        verbose_name="Transport / Transportation"
    )
    
    additional_info = models.TextField(
        blank=True,
        null=True,
        verbose_name="Inne informacje / Additional info",
        help_text="Inne ważne informacje o ofercie"
    )
    
    posted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data publikacji / Posted at"
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name="Aktywna / Active"
    )

    class Meta:
        verbose_name = "Oferta pracy / Job Posting"
        verbose_name_plural = "Oferty pracy / Job Postings"
        ordering = ['-posted_at']

    def __str__(self):
        return f"{self.title} at {self.company_name} ({self.location})"
    
    def get_salary_display_text(self):
        """Zwraca sformatowany tekst wynagrodzenia"""
        if self.salary_type == 'NEGOTIABLE':
            return "Do uzgodnienia / Negotiable"
        
        if self.salary_min and self.salary_max:
            return f"{self.salary_currency} {self.salary_min} - {self.salary_max}"
        elif self.salary_min:
            return f"Od {self.salary_currency} {self.salary_min}"
        elif self.salary_max:
            return f"Do {self.salary_currency} {self.salary_max}"
        else:
            return "Do uzgodnienia / Negotiable"