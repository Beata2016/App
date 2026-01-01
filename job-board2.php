<?php
session_start();

// Połączenie z bazą danych
$hostname = "localhost";
$database = "deb98572_ogloszenia";
$username = "deb98572_ogloszenia";
$password = "8Ecb7W3F4cJJMSh3K83c";

try {
    $pdo = new PDO("mysql:host=$hostname;dbname=$database;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("Connection error: " . $e->getMessage());
}

// ===== AJAX endpoint: sugestie dla pola 'job_role' (autocomplete) =====
if (isset($_GET['ajax']) && $_GET['ajax'] == '1' && isset($_GET['action']) && $_GET['action'] === 'role_suggest') {
    $q = trim($_GET['q'] ?? '');
    $out = [];
    if ($q !== '') {
        try {
            $like = "%{$q}%";
            $name_clauses = [];
            $name_params = [];
            foreach ($available_languages as $lg) {
                $col = "name_" . $lg;
                $name_clauses[] = "$col LIKE ?";
                $name_params[] = $like;
            }
            $sql = "SELECT id, name_$current_lang as name_local, name_en as name_en FROM job_categories WHERE (" . implode(' OR ', $name_clauses) . ") LIMIT 15";
            $stmt = $pdo->prepare($sql);
            $stmt->execute($name_params);
            $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
            foreach ($rows as $r) {
                $label = $r['name_local'] ?: $r['name_en'] ?: 'Category ' . $r['id'];
                $out[] = ['id' => $r['id'], 'label' => $label];
            }
        } catch (PDOException $e) {
            // ignore and return empty
        }
    }
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode($out);
    exit;
}

// Ustawienia językowe - 11 JĘZYKÓW
$available_languages = ['pl', 'nl', 'en', 'de', 'cs', 'ro', 'bg', 'hi', 'hu', 'ar', 'uk'];
$default_language = 'pl';

if (isset($_GET['lang']) && in_array($_GET['lang'], $available_languages)) {
    $_SESSION['lang'] = $_GET['lang'];
    // Przekieruj bez parametru lang w URL (zostanie w sesji)
    $params = $_GET;
    unset($params['lang']);
    $redirect_url = '?' . (!empty($params) ? http_build_query($params) : '');
    header('Location: ' . $redirect_url);
    exit;
} elseif (!isset($_SESSION['lang'])) {
    $_SESSION['lang'] = $default_language;
}

$current_lang = $_SESSION['lang'];

function getLanguageUrl($lang) {
    $params = $_GET;
    $params['lang'] = $lang;
    return '?' . http_build_query($params);
}

// Tłumaczenia - WSZYSTKIE 11 JĘZYKÓW
$translations = [
    'pl' => [
        'website_title' => 'HR Consulting Partner',
        'nav_home' => 'Strona główna',
        'nav_cv' => 'Baza CV',
        'nav_jobs' => 'Oferty pracy',
        'nav_companies' => 'Dla pracodawców',
        'nav_about' => 'O nas',
        'nav_contact' => 'Kontakt',
        'nav_ai' => '🤖 AI Chat',
        'hero_title' => 'Znajdź pracę swoich marzeń',
        'hero_subtitle' => 'Połącz się z najlepszymi pracodawcami w Holandii i całej Europie',
        'search_placeholder' => 'Stanowisko, słowa kluczowe lub firma...',
        'btn_search' => 'Szukaj',
        'filters_title' => 'Filtry wyszukiwania',
        'btn_clear' => 'Wyczyść wszystkie',
        'filter_country' => 'Kraj',
        'all_countries' => 'Wszystkie kraje',
        'filter_location' => 'Miasto',
        'all_cities' => 'Wszystkie miasta',
        'filter_region' => 'Region',
        'all_regions' => 'Wszystkie regiony',
        'filter_industry' => 'Branża',
        'all_industries' => 'Wszystkie branże',
        'filter_role' => 'Zawód',
        'all_roles' => 'Wszystkie zawody',
        'filter_type' => 'Typ umowy',
        'all_types' => 'Wszystkie typy',
        'filter_salary' => 'Wynagrodzenie min.',
        'all_salaries' => 'Dowolne wynagrodzenie',
        'filter_benefits' => 'Benefity',
        'filter_language' => 'Wymagania językowe',
        'all_languages' => 'Wszystkie języki',
        'filter_remote' => 'Praca zdalna',
        'all_remote' => 'Wszystkie opcje',
        'found' => 'Znaleziono',
        'offers' => 'ofert pracy',
        'sort_newest' => 'Najnowsze',
        'sort_salary' => 'Najwyższe wynagrodzenie',
        'btn_apply' => 'Aplikuj teraz',
        'btn_save' => 'Zapisz ofertę',
        'btn_details' => 'Szczegóły',
        'accommodation' => 'Zakwaterowanie',
        'transport' => 'Transport',
        'meals' => 'Wyżywienie',
        'visa' => 'Pomoc wizowa',
        'urgent' => 'Pilne',
        'week' => 'tydz',
        'no_results_title' => 'Brak wyników',
        'no_results_text' => 'Spróbuj zmienić kryteria wyszukiwania',
        'salary_range' => 'Wynagrodzenie',
        'location' => 'Lokalizacja',
        'employment_type' => 'Typ zatrudnienia',
        'date_posted' => 'Data publikacji',
        'requirements' => 'Wymagania',
        'language_requirement' => 'Wymagania językowe',
        'remote_option_none' => 'Praca stacjonarna',
        'remote_option_partial' => 'Hybrydowa',
        'remote_option_full' => 'W pełni zdalna',
        'apply_via_whatsapp' => 'Aplikuj przez WhatsApp',
        'apply_via_website' => 'Aplikuj przez formularz',
        'apply_via_email' => 'Wyślij CV na email',
        'contact_options' => 'Wybierz sposób aplikacji',
        'whatsapp_number' => '0031657558110',
        'view_all' => 'Zobacz wszystkie',
        'featured_jobs' => 'Wyróżnione oferty',
        'popular_categories' => 'Popularne kategorie',
        'recent_jobs' => 'Ostatnie oferty',
        'page' => 'Strona',
        'of' => 'z',
        'prev' => 'Poprzednia',
        'next' => 'Następna',
        'show_all' => 'Pokaż wszystkie',
        'items_per_page' => 'Liczba ofert na stronie',
    ],
    'nl' => [
        'website_title' => 'HR Consulting Partner',
        'nav_home' => 'Home',
        'nav_cv' => 'CV Database',
        'nav_jobs' => 'Vacatures',
        'nav_companies' => 'Voor bedrijven',
        'nav_about' => 'Over ons',
        'nav_contact' => 'Contact',
        'nav_ai' => '🤖 AI Chat',
        'hero_title' => 'Vind je droombaan',
        'hero_subtitle' => 'Verbinden met de beste werkgevers in Nederland en heel Europa',
        'search_placeholder' => 'Functie, trefwoord of bedrijf...',
        'btn_search' => 'Zoeken',
        'filters_title' => 'Zoekfilters',
        'btn_clear' => 'Alles wissen',
        'filter_country' => 'Land',
        'all_countries' => 'Alle landen',
        'filter_location' => 'Stad',
        'all_cities' => 'Alle steden',
        'filter_region' => 'Regio',
        'all_regions' => 'Alle regios',
        'filter_industry' => 'Industrie',
        'all_industries' => 'Alle industrieën',
        'filter_role' => 'Beroep',
        'all_roles' => 'Alle beroepen',
        'filter_type' => 'Contracttype',
        'all_types' => 'Alle contracten',
        'filter_salary' => 'Min. salaris',
        'all_salaries' => 'Elk salaris',
        'filter_benefits' => 'Secundaire voorwaarden',
        'filter_language' => 'Taalvereisten',
        'all_languages' => 'Alle talen',
        'filter_remote' => 'Remote werk',
        'all_remote' => 'Alle opties',
        'found' => 'Gevonden',
        'offers' => 'vacatures',
        'sort_newest' => 'Nieuwste',
        'sort_salary' => 'Hoogste salaris',
        'btn_apply' => 'Solliciteer nu',
        'btn_save' => 'Opslaan',
        'btn_details' => 'Details',
        'accommodation' => 'Accommodatie',
        'transport' => 'Vervoer',
        'meals' => 'Maaltijden',
        'visa' => 'Visum hulp',
        'urgent' => 'Spoed',
        'week' => 'week',
        'no_results_title' => 'Geen resultaten',
        'no_results_text' => 'Probeer andere zoekcriteria',
        'salary_range' => 'Salaris',
        'location' => 'Locatie',
        'employment_type' => 'Dienstverband',
        'date_posted' => 'Publicatiedatum',
        'requirements' => 'Vereisten',
        'language_requirement' => 'Taalvereisten',
        'remote_option_none' => 'Kantoor werk',
        'remote_option_partial' => 'Hybride',
        'remote_option_full' => 'Volledig remote',
        'apply_via_whatsapp' => 'Solliciteer via WhatsApp',
        'apply_via_website' => 'Solliciteer via formulier',
        'apply_via_email' => 'Stuur CV per email',
        'contact_options' => 'Kies sollicitatiewijze',
        'whatsapp_number' => '0031657558110',
        'view_all' => 'Bekijk alle',
        'featured_jobs' => 'Uitgelichte vacatures',
        'popular_categories' => 'Populaire categorieën',
        'recent_jobs' => 'Recente vacatures',
        'page' => 'Pagina',
        'of' => 'van',
        'prev' => 'Vorige',
        'next' => 'Volgende',
        'show_all' => 'Toon alle',
        'items_per_page' => 'Vacatures per pagina',
    ],
    'en' => [
        'website_title' => 'HR Consulting Partner',
        'nav_home' => 'Home',
        'nav_cv' => 'CV Database',
        'nav_jobs' => 'Job Offers',
        'nav_companies' => 'For Employers',
        'nav_about' => 'About Us',
        'nav_contact' => 'Contact',
        'nav_ai' => '🤖 AI Chat',
        'hero_title' => 'Find Your Dream Job',
        'hero_subtitle' => 'Connect with the best employers in the Netherlands and across Europe',
        'search_placeholder' => 'Position, keywords or company...',
        'btn_search' => 'Search',
        'filters_title' => 'Search Filters',
        'btn_clear' => 'Clear All',
        'filter_country' => 'Country',
        'all_countries' => 'All Countries',
        'filter_location' => 'City',
        'all_cities' => 'All Cities',
        'filter_region' => 'Region',
        'all_regions' => 'All Regions',
        'filter_industry' => 'Industry',
        'all_industries' => 'All Industries',
        'filter_role' => 'Profession',
        'all_roles' => 'All Professions',
        'filter_type' => 'Contract Type',
        'all_types' => 'All Types',
        'filter_salary' => 'Min. Salary',
        'all_salaries' => 'Any Salary',
        'filter_benefits' => 'Benefits',
        'filter_language' => 'Language Requirements',
        'all_languages' => 'All Languages',
        'filter_remote' => 'Remote Work',
        'all_remote' => 'All Options',
        'found' => 'Found',
        'offers' => 'job offers',
        'sort_newest' => 'Newest',
        'sort_salary' => 'Highest Salary',
        'btn_apply' => 'Apply Now',
        'btn_save' => 'Save Offer',
        'btn_details' => 'Details',
        'accommodation' => 'Accommodation',
        'transport' => 'Transport',
        'meals' => 'Meals',
        'visa' => 'Visa Assistance',
        'urgent' => 'Urgent',
        'week' => 'week',
        'no_results_title' => 'No Results',
        'no_results_text' => 'Try changing your search criteria',
        'salary_range' => 'Salary',
        'location' => 'Location',
        'employment_type' => 'Employment Type',
        'date_posted' => 'Date Posted',
        'requirements' => 'Requirements',
        'language_requirement' => 'Language Requirements',
        'remote_option_none' => 'Office Work',
        'remote_option_partial' => 'Hybrid',
        'remote_option_full' => 'Fully Remote',
        'apply_via_whatsapp' => 'Apply via WhatsApp',
        'apply_via_website' => 'Apply via form',
        'apply_via_email' => 'Send CV by email',
        'contact_options' => 'Choose application method',
        'whatsapp_number' => '0031657558110',
        'view_all' => 'View All',
        'featured_jobs' => 'Featured Jobs',
        'popular_categories' => 'Popular Categories',
        'recent_jobs' => 'Recent Jobs',
        'page' => 'Page',
        'of' => 'of',
        'prev' => 'Previous',
        'next' => 'Next',
        'show_all' => 'Show all',
        'items_per_page' => 'Items per page',
    ],
    'de' => [
        'website_title' => 'HR Consulting Partner',
        'nav_home' => 'Startseite',
        'nav_cv' => 'CV-Datenbank',
        'nav_jobs' => 'Stellenangebote',
        'nav_companies' => 'Für Arbeitgeber',
        'nav_about' => 'Über uns',
        'nav_contact' => 'Kontakt',
        'nav_ai' => '🤖 AI Chat',
        'hero_title' => 'Finden Sie Ihren Traumjob',
        'hero_subtitle' => 'Verbinden Sie sich mit den besten Arbeitgebern in den Niederlanden und ganz Europa',
        'search_placeholder' => 'Position, Stichwörter oder Unternehmen...',
        'btn_search' => 'Suchen',
        'filters_title' => 'Suchfilter',
        'btn_clear' => 'Alle löschen',
        'filter_country' => 'Land',
        'all_countries' => 'Alle Länder',
        'filter_location' => 'Stadt',
        'all_cities' => 'Alle Städte',
        'filter_region' => 'Region',
        'all_regions' => 'Alle Regionen',
        'filter_industry' => 'Branche',
        'all_industries' => 'Alle Branchen',
        'filter_role' => 'Beruf',
        'all_roles' => 'Alle Berufe',
        'filter_type' => 'Vertragsart',
        'all_types' => 'Alle Arten',
        'filter_salary' => 'Mindestgehalt',
        'all_salaries' => 'Beliebiges Gehalt',
        'filter_benefits' => 'Leistungen',
        'filter_language' => 'Sprachanforderungen',
        'all_languages' => 'Alle Sprachen',
        'filter_remote' => 'Remote Arbeit',
        'all_remote' => 'Alle Optionen',
        'found' => 'Gefunden',
        'offers' => 'Stellenangebote',
        'sort_newest' => 'Neueste',
        'sort_salary' => 'Höchstes Gehalt',
        'btn_apply' => 'Jetzt bewerben',
        'btn_save' => 'Angebot speichern',
        'btn_details' => 'Details',
        'accommodation' => 'Unterkunft',
        'transport' => 'Transport',
        'meals' => 'Verpflegung',
        'visa' => 'Visumunterstützung',
        'urgent' => 'Dringend',
        'week' => 'Woche',
        'no_results_title' => 'Keine Ergebnisse',
        'no_results_text' => 'Versuchen Sie, Ihre Suchkriterien zu ändern',
        'salary_range' => 'Gehalt',
        'location' => 'Standort',
        'employment_type' => 'Beschäftigungsart',
        'date_posted' => 'Veröffentlichungsdatum',
        'requirements' => 'Anforderungen',
        'language_requirement' => 'Sprachanforderungen',
        'remote_option_none' => 'Büroarbeit',
        'remote_option_partial' => 'Hybrid',
        'remote_option_full' => 'Vollständig remote',
        'apply_via_whatsapp' => 'Bewerben via WhatsApp',
        'apply_via_website' => 'Bewerben via Formular',
        'apply_via_email' => 'CV per E-Mail senden',
        'contact_options' => 'Bewerbungsmethode wählen',
        'whatsapp_number' => '0031657558110',
        'view_all' => 'Alle ansehen',
        'featured_jobs' => 'Empfohlene Jobs',
        'popular_categories' => 'Beliebte Kategorien',
        'recent_jobs' => 'Aktuelle Jobs',
        'page' => 'Seite',
        'of' => 'von',
        'prev' => 'Zurück',
        'next' => 'Weiter',
        'show_all' => 'Alle anzeigen',
        'items_per_page' => 'Angebote pro Seite',
    ],
    'cs' => [
        'website_title' => 'HR Consulting Partner',
        'nav_home' => 'Domů',
        'nav_cv' => 'CV Databáze',
        'nav_jobs' => 'Pracovní nabídky',
        'nav_companies' => 'Pro zaměstnavatele',
        'nav_about' => 'O nás',
        'nav_contact' => 'Kontakt',
        'nav_ai' => '🤖 AI Chat',
        'hero_title' => 'Najděte práci svých snů',
        'hero_subtitle' => 'Spojte se s nejlepšími zaměstnavateli v Nizozemsku a celé Evropě',
        'search_placeholder' => 'Pozice, klíčová slova nebo společnost...',
        'btn_search' => 'Hledat',
        'filters_title' => 'Filtry vyhledávání',
        'btn_clear' => 'Vymazat vše',
        'filter_country' => 'Země',
        'all_countries' => 'Všechny země',
        'filter_location' => 'Město',
        'all_cities' => 'Všechna města',
        'filter_region' => 'Region',
        'all_regions' => 'Všechny regiony',
        'filter_industry' => 'Průmysl',
        'all_industries' => 'Všechna odvětví',
        'filter_role' => 'Profese',
        'all_roles' => 'Všechny profese',
        'filter_type' => 'Typ smlouvy',
        'all_types' => 'Všechny typy',
        'filter_salary' => 'Min. plat',
        'all_salaries' => 'Jakýkoli plat',
        'filter_benefits' => 'Benefity',
        'filter_language' => 'Jazykové požadavky',
        'all_languages' => 'Všechny jazyky',
        'filter_remote' => 'Práce na dálku',
        'all_remote' => 'Všechny možnosti',
        'found' => 'Nalezeno',
        'offers' => 'pracovních nabídek',
        'sort_newest' => 'Nejnovější',
        'sort_salary' => 'Nejvyšší plat',
        'btn_apply' => 'Aplikovat nyní',
        'btn_save' => 'Uložit nabídku',
        'btn_details' => 'Podrobnosti',
        'accommodation' => 'Ubytování',
        'transport' => 'Doprava',
        'meals' => 'Stravování',
        'visa' => 'Vízová pomoc',
        'urgent' => 'Naléhavé',
        'week' => 'týden',
        'no_results_title' => 'Žádné výsledky',
        'no_results_text' => 'Zkuste změnit kritéria vyhledávání',
        'salary_range' => 'Plat',
        'location' => 'Poloha',
        'employment_type' => 'Typ zaměstnání',
        'date_posted' => 'Datum zveřejnění',
        'requirements' => 'Požadavky',
        'language_requirement' => 'Jazykové požadavky',
        'remote_option_none' => 'Kancelářská práce',
        'remote_option_partial' => 'Hybridní',
        'remote_option_full' => 'Plně vzdálená',
        'apply_via_whatsapp' => 'Aplikovat přes WhatsApp',
        'apply_via_website' => 'Aplikovat přes formulář',
        'apply_via_email' => 'Poslat CV e-mailem',
        'contact_options' => 'Vyberte způsob aplikace',
        'whatsapp_number' => '0031657558110',
        'view_all' => 'Zobrazit vše',
        'featured_jobs' => 'Doporučené nabídky',
        'popular_categories' => 'Populární kategorie',
        'recent_jobs' => 'Nedávné nabídky',
        'page' => 'Stránka',
        'of' => 'z',
        'prev' => 'Předchozí',
        'next' => 'Další',
        'show_all' => 'Zobrazit vše',
        'items_per_page' => 'Počet nabídek na stránce',
    ],
    'ro' => [
        'website_title' => 'HR Consulting Partner',
        'nav_home' => 'Acasă',
        'nav_cv' => 'Baza de CV-uri',
        'nav_jobs' => 'Oferte de muncă',
        'nav_companies' => 'Pentru angajatori',
        'nav_about' => 'Despre noi',
        'nav_contact' => 'Contact',
        'nav_ai' => '🤖 AI Chat',
        'hero_title' => 'Găsiți slujba visurilor dumneavoastră',
        'hero_subtitle' => 'Conectați-vă cu cei mai buni angajatori din Olanda și întreaga Europă',
        'search_placeholder' => 'Poziție, cuvinte cheie sau companie...',
        'btn_search' => 'Căutare',
        'filters_title' => 'Filtre de căutare',
        'btn_clear' => 'Șterge tot',
        'filter_country' => 'Țară',
        'all_countries' => 'Toate țările',
        'filter_location' => 'Oraș',
        'all_cities' => 'Toate orașele',
        'filter_region' => 'Regiune',
        'all_regions' => 'Toate regiunile',
        'filter_industry' => 'Industrie',
        'all_industries' => 'Toate industriile',
        'filter_role' => 'Profesie',
        'all_roles' => 'Toate profesiile',
        'filter_type' => 'Tip contract',
        'all_types' => 'Toate tipurile',
        'filter_salary' => 'Salariu min.',
        'all_salaries' => 'Orice salariu',
        'filter_benefits' => 'Beneficii',
        'filter_language' => 'Cerințe lingvistice',
        'all_languages' => 'Toate limbile',
        'filter_remote' => 'Munca la distanță',
        'all_remote' => 'Toate opțiunile',
        'found' => 'Găsite',
        'offers' => 'oferte de muncă',
        'sort_newest' => 'Cele mai noi',
        'sort_salary' => 'Cel mai mare salariu',
        'btn_apply' => 'Aplică acum',
        'btn_save' => 'Salvează oferta',
        'btn_details' => 'Detalii',
        'accommodation' => 'Cazare',
        'transport' => 'Transport',
        'meals' => 'Mese',
        'visa' => 'Asistență viză',
        'urgent' => 'Urgent',
        'week' => 'săptămână',
        'no_results_title' => 'Niciun rezultat',
        'no_results_text' => 'Încercați să schimbați criteriile de căutare',
        'salary_range' => 'Salariu',
        'location' => 'Locație',
        'employment_type' => 'Tip angajare',
        'date_posted' => 'Data postării',
        'requirements' => 'Cerințe',
        'language_requirement' => 'Cerințe lingvistice',
        'remote_option_none' => 'Munca la birou',
        'remote_option_partial' => 'Hibrid',
        'remote_option_full' => 'Complet la distanță',
        'apply_via_whatsapp' => 'Aplicați prin WhatsApp',
        'apply_via_website' => 'Aplicați prin formular',
        'apply_via_email' => 'Trimiteți CV pe email',
        'contact_options' => 'Alegeți metoda de aplicare',
        'whatsapp_number' => '0031657558110',
        'view_all' => 'Vezi toate',
        'featured_jobs' => 'Oferte recomandate',
        'popular_categories' => 'Categorii populare',
        'recent_jobs' => 'Oferte recente',
        'page' => 'Pagina',
        'of' => 'din',
        'prev' => 'Anterior',
        'next' => 'Următor',
        'show_all' => 'Afișează toate',
        'items_per_page' => 'Oferte pe pagină',
    ],
    'bg' => [
        'website_title' => 'HR Consulting Partner',
        'nav_home' => 'Начало',
        'nav_cv' => 'CV База',
        'nav_jobs' => 'Работни Обяви',
        'nav_companies' => 'За работодатели',
        'nav_about' => 'За нас',
        'nav_contact' => 'Контакт',
        'nav_ai' => '🤖 AI Chat',
        'hero_title' => 'Намерете работата на мечтите си',
        'hero_subtitle' => 'Свържете се с най-добрите работодатели в Холандия и цяла Европа',
        'search_placeholder' => 'Длъжност, ключови думи или компания...',
        'btn_search' => 'Търсене',
        'filters_title' => 'Филтри за търсене',
        'btn_clear' => 'Изчисти всички',
        'filter_country' => 'Държава',
        'all_countries' => 'Всички държави',
        'filter_location' => 'Град',
        'all_cities' => 'Всички градове',
        'filter_region' => 'Регион',
        'all_regions' => 'Всички региони',
        'filter_industry' => 'Индустрия',
        'all_industries' => 'Всички индустрии',
        'filter_role' => 'Професия',
        'all_roles' => 'Всички професии',
        'filter_type' => 'Тип договор',
        'all_types' => 'Всички типове',
        'filter_salary' => 'Мин. заплата',
        'all_salaries' => 'Всяка заплата',
        'filter_benefits' => 'Облекчения',
        'filter_language' => 'Езикови изисквания',
        'all_languages' => 'Всички езици',
        'filter_remote' => 'Дистанционна работа',
        'all_remote' => 'Всички опции',
        'found' => 'Намерени',
        'offers' => 'работни обяви',
        'sort_newest' => 'Най-нови',
        'sort_salary' => 'Най-висока заплата',
        'btn_apply' => 'Кандидатствай сега',
        'btn_save' => 'Запази обява',
        'btn_details' => 'Детайли',
        'accommodation' => 'Настаняване',
        'transport' => 'Транспорт',
        'meals' => 'Хранене',
        'visa' => 'Визова помощ',
        'urgent' => 'Спешно',
        'week' => 'седмица',
        'no_results_title' => 'Няма резултати',
        'no_results_text' => 'Опитайте да промените критериите за търсене',
        'salary_range' => 'Заплата',
        'location' => 'Местоположение',
        'employment_type' => 'Вид заетост',
        'date_posted' => 'Дата на публикуване',
        'requirements' => 'Изисквания',
        'language_requirement' => 'Езикови изисквания',
        'remote_option_none' => 'Офис работа',
        'remote_option_partial' => 'Хибридна',
        'remote_option_full' => 'Напълно дистанционна',
        'apply_via_whatsapp' => 'Кандидатствайте чрез WhatsApp',
        'apply_via_website' => 'Кандидатствайте чрез формуляр',
        'apply_via_email' => 'Изпратете CV по имейл',
        'contact_options' => 'Изберете начин на кандидатстване',
        'whatsapp_number' => '0031657558110',
        'view_all' => 'Вижте всички',
        'featured_jobs' => 'Препоръчани обяви',
        'popular_categories' => 'Популярни категории',
        'recent_jobs' => 'Скорошни обяви',
        'page' => 'Страница',
        'of' => 'от',
        'prev' => 'Предишна',
        'next' => 'Следваща',
        'show_all' => 'Покажи всички',
        'items_per_page' => 'Обяви на страница',
    ],
    'hi' => [
        'website_title' => 'HR Consulting Partner',
        'nav_home' => 'होम',
        'nav_cv' => 'सीवी डेटाबेस',
        'nav_jobs' => 'नौकरी के अवसर',
        'nav_companies' => 'नियोक्ताओं के लिए',
        'nav_about' => 'हमारे बारे में',
        'nav_contact' => 'संपर्क करें',
        'nav_ai' => '🤖 AI चैट',
        'hero_title' => 'अपने सपनों की नौकरी पाएं',
        'hero_subtitle' => 'नीदरलैंड और पूरे यूरोप में सर्वश्रेष्ठ नियोक्ताओं से जुड़ें',
        'search_placeholder' => 'पद, कीवर्ड या कंपनी...',
        'btn_search' => 'खोजें',
        'filters_title' => 'खोज फिल्टर',
        'btn_clear' => 'सभी साफ करें',
        'filter_country' => 'देश',
        'all_countries' => 'सभी देश',
        'filter_location' => 'शहर',
        'all_cities' => 'सभी शहर',
        'filter_region' => 'क्षेत्र',
        'all_regions' => 'सभी क्षेत्र',
        'filter_industry' => 'उद्योग',
        'all_industries' => 'सभी उद्योग',
        'filter_role' => 'पेशा',
        'all_roles' => 'सभी पेशे',
        'filter_type' => 'अनुबंध प्रकार',
        'all_types' => 'सभी प्रकार',
        'filter_salary' => 'न्यूनतम वेतन',
        'all_salaries' => 'कोई भी वेतन',
        'filter_benefits' => 'लाभ',
        'filter_language' => 'भाषा आवश्यकताएं',
        'all_languages' => 'सभी भाषाएं',
        'filter_remote' => 'दूरस्थ कार्य',
        'all_remote' => 'सभी विकल्प',
        'found' => 'मिला',
        'offers' => 'नौकरी के अवसर',
        'sort_newest' => 'नवीनतम',
        'sort_salary' => 'उच्चतम वेतन',
        'btn_apply' => 'अभी आवेदन करें',
        'btn_save' => 'ऑफर सहेजें',
        'btn_details' => 'विवरण',
        'accommodation' => 'आवास',
        'transport' => 'परिवहन',
        'meals' => 'भोजन',
        'visa' => 'वीज़ा सहायता',
        'urgent' => 'जरूरी',
        'week' => 'सप्ताह',
        'no_results_title' => 'कोई परिणाम नहीं',
        'no_results_text' => 'अपने खोज मानदंड बदलने का प्रयास करें',
        'salary_range' => 'वेतन',
        'location' => 'स्थान',
        'employment_type' => 'रोजगार प्रकार',
        'date_posted' => 'पोस्ट की तारीख',
        'requirements' => 'आवश्यकताएं',
        'language_requirement' => 'भाषा आवश्यकताएं',
        'remote_option_none' => 'कार्यालय कार्य',
        'remote_option_partial' => 'हाइब्रिड',
        'remote_option_full' => 'पूरी तरह से दूरस्थ',
        'apply_via_whatsapp' => 'WhatsApp के माध्यम से आवेदन करें',
        'apply_via_website' => 'फॉर्म के माध्यम से आवेदन करें',
        'apply_via_email' => 'ईमेल द्वारा सीवी भेजें',
        'contact_options' => 'आवेदन विधि चुनें',
        'whatsapp_number' => '0031657558110',
        'view_all' => 'सभी देखें',
        'featured_jobs' => 'विशेष नौकरियां',
        'popular_categories' => 'लोकप्रिय श्रेणियां',
        'recent_jobs' => 'हाल की नौकरियां',
        'page' => 'पृष्ठ',
        'of' => 'का',
        'prev' => 'पिछला',
        'next' => 'अगला',
        'show_all' => 'सभी दिखाएं',
        'items_per_page' => 'प्रति पृष्ठ आइटम',
    ],
    'hu' => [
        'website_title' => 'HR Consulting Partner',
        'nav_home' => 'Kezdőlap',
        'nav_cv' => 'CV Adatbázis',
        'nav_jobs' => 'Állásajánlatok',
        'nav_companies' => 'Munkáltatóknak',
        'nav_about' => 'Rólunk',
        'nav_contact' => 'Kapcsolat',
        'nav_ai' => '🤖 AI Chat',
        'hero_title' => 'Találd meg álmaid állását',
        'hero_subtitle' => 'Kapcsolódj a legjobb munkáltatókhoz Hollandiában és egész Európában',
        'search_placeholder' => 'Pozíció, kulcsszavak vagy cég...',
        'btn_search' => 'Keresés',
        'filters_title' => 'Keresési szűrők',
        'btn_clear' => 'Összes törlése',
        'filter_country' => 'Ország',
        'all_countries' => 'Minden ország',
        'filter_location' => 'Város',
        'all_cities' => 'Minden város',
        'filter_region' => 'Régió',
        'all_regions' => 'Minden régió',
        'filter_industry' => 'Iparág',
        'all_industries' => 'Minden iparág',
        'filter_role' => 'Szakma',
        'all_roles' => 'Minden szakma',
        'filter_type' => 'Szerződés típusa',
        'all_types' => 'Minden típus',
        'filter_salary' => 'Min. fizetés',
        'all_salaries' => 'Bármilyen fizetés',
        'filter_benefits' => 'Juttatások',
        'filter_language' => 'Nyelvi követelmények',
        'all_languages' => 'Minden nyelv',
        'filter_remote' => 'Távmunka',
        'all_remote' => 'Minden lehetőség',
        'found' => 'Találat',
        'offers' => 'állásajánlat',
        'sort_newest' => 'Legújabb',
        'sort_salary' => 'Legmagasabb fizetés',
        'btn_apply' => 'Jelentkezés most',
        'btn_save' => 'Ajánlat mentése',
        'btn_details' => 'Részletek',
        'accommodation' => 'Szállás',
        'transport' => 'Közlekedés',
        'meals' => 'Étkezés',
        'visa' => 'Vízumsegítség',
        'urgent' => 'Sürgős',
        'week' => 'hét',
        'no_results_title' => 'Nincs találat',
        'no_results_text' => 'Próbáld megváltoztatni a keresési feltételeket',
        'salary_range' => 'Fizetés',
        'location' => 'Helyszín',
        'employment_type' => 'Foglalkoztatás típusa',
        'date_posted' => 'Közzétéve',
        'requirements' => 'Követelmények',
        'language_requirement' => 'Nyelvi követelmények',
        'remote_option_none' => 'Irodai munka',
        'remote_option_partial' => 'Hibrid',
        'remote_option_full' => 'Teljesen távmunka',
        'apply_via_whatsapp' => 'Jelentkezés WhatsApp-on keresztül',
        'apply_via_website' => 'Jelentkezés űrlapon keresztül',
        'apply_via_email' => 'CV küldése e-mailben',
        'contact_options' => 'Válassz jelentkezési módot',
        'whatsapp_number' => '0031657558110',
        'view_all' => 'Összes megtekintése',
        'featured_jobs' => 'Kiemelt állások',
        'popular_categories' => 'Népszerű kategóriák',
        'recent_jobs' => 'Friss állások',
        'page' => 'Oldal',
        'of' => 'az',
        'prev' => 'Előző',
        'next' => 'Következő',
        'show_all' => 'Összes mutatása',
        'items_per_page' => 'Elemek oldalanként',
    ],
    'ar' => [
        'website_title' => 'HR Consulting Partner',
        'nav_home' => 'الرئيسية',
        'nav_cv' => 'قاعدة بيانات السيرة الذاتية',
        'nav_jobs' => 'عروض العمل',
        'nav_companies' => 'لأصحاب العمل',
        'nav_about' => 'من نحن',
        'nav_contact' => 'اتصل بنا',
        'nav_ai' => '🤖 AI دردشة',
        'hero_title' => 'ابحث عن وظيفة أحلامك',
        'hero_subtitle' => 'تواصل مع أفضل أصحاب العمل في هولندا وعبر أوروبا',
        'search_placeholder' => 'المنصب، الكلمات الرئيسية أو الشركة...',
        'btn_search' => 'بحث',
        'filters_title' => 'مرشحات البحث',
        'btn_clear' => 'مسح الكل',
        'filter_country' => 'الدولة',
        'all_countries' => 'جميع الدول',
        'filter_location' => 'المدينة',
        'all_cities' => 'جميع المدن',
        'filter_region' => 'المنطقة',
        'all_regions' => 'جميع المناطق',
        'filter_industry' => 'الصناعة',
        'all_industries' => 'جميع الصناعات',
        'filter_role' => 'المهنة',
        'all_roles' => 'جميع المهن',
        'filter_type' => 'نوع العقد',
        'all_types' => 'جميع الأنواع',
        'filter_salary' => 'الحد الأدنى للراتب',
        'all_salaries' => 'أي راتب',
        'filter_benefits' => 'المزايا',
        'filter_language' => 'متطلبات اللغة',
        'all_languages' => 'جميع اللغات',
        'filter_remote' => 'العمل عن بُعد',
        'all_remote' => 'جميع الخيارات',
        'found' => 'تم العثور على',
        'offers' => 'عرض عمل',
        'sort_newest' => 'الأحدث',
        'sort_salary' => 'أعلى راتب',
        'btn_apply' => 'قدم الآن',
        'btn_save' => 'حفظ العرض',
        'btn_details' => 'التفاصيل',
        'accommodation' => 'الإقامة',
        'transport' => 'النقل',
        'meals' => 'الوجبات',
        'visa' => 'مساعدة التأشيرة',
        'urgent' => 'عاجل',
        'week' => 'أسبوع',
        'no_results_title' => 'لا توجد نتائج',
        'no_results_text' => 'حاول تغيير معايير البحث',
        'salary_range' => 'الراتب',
        'location' => 'الموقع',
        'employment_type' => 'نوع التوظيف',
        'date_posted' => 'تاريخ النشر',
        'requirements' => 'المتطلبات',
        'language_requirement' => 'متطلبات اللغة',
        'remote_option_none' => 'عمل مكتبي',
        'remote_option_partial' => 'هجين',
        'remote_option_full' => 'عن بُعد بالكامل',
        'apply_via_whatsapp' => 'تقديم عبر واتساب',
        'apply_via_website' => 'تقديم عبر النموذج',
        'apply_via_email' => 'إرسال السيرة الذاتية بالبريد الإلكتروني',
        'contact_options' => 'اختر طريقة التقديم',
        'whatsapp_number' => '0031657558110',
        'view_all' => 'عرض الكل',
        'featured_jobs' => 'وظائف مميزة',
        'popular_categories' => 'الفئات الشائعة',
        'recent_jobs' => 'الوظائف الأخيرة',
        'page' => 'صفحة',
        'of' => 'من',
        'prev' => 'السابق',
        'next' => 'التالي',
        'show_all' => 'عرض الكل',
        'items_per_page' => 'عناصر في الصفحة',
    ],
    'uk' => [
        'website_title' => 'HR Consulting Partner',
        'nav_home' => 'Головна',
        'nav_cv' => 'База CV',
        'nav_jobs' => 'Вакансії',
        'nav_companies' => 'Для роботодавців',
        'nav_about' => 'Про нас',
        'nav_contact' => 'Контакти',
        'nav_ai' => '🤖 AI Chat',
        'hero_title' => 'Знайдіть роботу своєї мрії',
        'hero_subtitle' => 'Зв\'яжіться з найкращими роботодавцями в Нідерландах та по всій Європі',
        'search_placeholder' => 'Посада, ключові слова або компанія...',
        'btn_search' => 'Пошук',
        'filters_title' => 'Фільтри пошуку',
        'btn_clear' => 'Очистити все',
        'filter_country' => 'Країна',
        'all_countries' => 'Всі країни',
        'filter_location' => 'Місто',
        'all_cities' => 'Всі міста',
        'filter_region' => 'Регіон',
        'all_regions' => 'Всі регіони',
        'filter_industry' => 'Галузь',
        'all_industries' => 'Всі галузі',
        'filter_role' => 'Професія',
        'all_roles' => 'Всі професії',
        'filter_type' => 'Тип контракту',
        'all_types' => 'Всі типи',
        'filter_salary' => 'Мін. заробітна плата',
        'all_salaries' => 'Будь-яка зарплата',
        'filter_benefits' => 'Пільги',
        'filter_language' => 'Мовні вимоги',
        'all_languages' => 'Всі мови',
        'filter_remote' => 'Віддалена робота',
        'all_remote' => 'Всі варіанти',
        'found' => 'Знайдено',
        'offers' => 'вакансій',
        'sort_newest' => 'Найновіші',
        'sort_salary' => 'Найвища зарплата',
        'btn_apply' => 'Подати заявку',
        'btn_save' => 'Зберегти пропозицію',
        'btn_details' => 'Деталі',
        'accommodation' => 'Житло',
        'transport' => 'Транспорт',
        'meals' => 'Харчування',
        'visa' => 'Візова допомога',
        'urgent' => 'Терміново',
        'week' => 'тиждень',
        'no_results_title' => 'Результатів не знайдено',
        'no_results_text' => 'Спробуйте змінити критерії пошуку',
        'salary_range' => 'Зарплата',
        'location' => 'Місцезнаходження',
        'employment_type' => 'Тип зайнятості',
        'date_posted' => 'Дата публікації',
        'requirements' => 'Вимоги',
        'language_requirement' => 'Мовні вимоги',
        'remote_option_none' => 'Офісна робота',
        'remote_option_partial' => 'Гібридна',
        'remote_option_full' => 'Повністю віддалена',
        'apply_via_whatsapp' => 'Подати заявку через WhatsApp',
        'apply_via_website' => 'Подати заявку через форму',
        'apply_via_email' => 'Надіслати CV по email',
        'contact_options' => 'Виберіть спосіб подачі заявки',
        'whatsapp_number' => '0031657558110',
        'view_all' => 'Переглянути всі',
        'featured_jobs' => 'Рекомендовані вакансії',
        'popular_categories' => 'Популярні категорії',
        'recent_jobs' => 'Останні вакансії',
        'page' => 'Сторінка',
        'of' => 'з',
        'prev' => 'Попередня',
        'next' => 'Наступна',
        'show_all' => 'Показати всі',
        'items_per_page' => 'Пропозицій на сторінці',
    ]
];

function t($key) {
    global $translations, $current_lang;
    return $translations[$current_lang][$key] ?? $translations['en'][$key] ?? $key;
}

// Pobierz dane dla list rozwijanych z bazy (z tłumaczeniami)
try {
    // ZMIANA: Wszystkie kraje z bazy danych - posortowane alfabetycznie
    $countries_stmt = $pdo->query("SELECT id, name_en, name_$current_lang FROM countries ORDER BY name_en");
    $all_countries = $countries_stmt->fetchAll(PDO::FETCH_ASSOC);
    
    // Regiony z bazy danych
    $regions_stmt = $pdo->query("SELECT DISTINCT region FROM job_offers WHERE region IS NOT NULL AND region != '' ORDER BY region");
    $regions = $regions_stmt->fetchAll(PDO::FETCH_COLUMN, 0);
    
    // Miasta z bazy danych
    $cities_stmt = $pdo->query("SELECT DISTINCT city FROM job_offers WHERE city IS NOT NULL AND city != '' ORDER BY city");
    $dutch_cities = $cities_stmt->fetchAll(PDO::FETCH_COLUMN, 0);
    
    // Branże z bazy danych
    $industries_stmt = $pdo->query("SELECT id, name_$current_lang as name FROM industries ORDER BY name");
    $industries = $industries_stmt->fetchAll(PDO::FETCH_ASSOC);
    
    // Kategorie zawodów z bazy danych
    $categories_stmt = $pdo->query("SELECT id, name_$current_lang as name FROM job_categories WHERE parent_id = 0 ORDER BY name");
    $job_categories = $categories_stmt->fetchAll(PDO::FETCH_ASSOC);
    
    // Typy umów z bazy danych
    $contracts_stmt = $pdo->query("SELECT code, name_$current_lang as name FROM employment_types ORDER BY name");
    $contract_types = $contracts_stmt->fetchAll(PDO::FETCH_ASSOC);
    
    // Wymagania językowe z bazy danych
    $language_stmt = $pdo->query("SELECT code, name_$current_lang as name FROM language_requirements ORDER BY name");
    $language_requirements = $language_stmt->fetchAll(PDO::FETCH_ASSOC);
    
    // Range dla wynagrodzeń
    $salary_ranges = [
        ['value' => '', 'label' => t('all_salaries')],
        ['value' => '1500', 'label' => '€1,500+'],
        ['value' => '2000', 'label' => '€2,000+'],
        ['value' => '2500', 'label' => '€2,500+'],
        ['value' => '3000', 'label' => '€3,000+'],
        ['value' => '3500', 'label' => '€3,500+'],
        ['value' => '4000', 'label' => '€4,000+'],
    ];
    
} catch(PDOException $e) {
    $all_countries = [];
    $regions = [];
    $dutch_cities = [];
    $industries = [];
    $job_categories = [];
    $contract_types = [];
    $language_requirements = [];
    $salary_ranges = [
        ['value' => '', 'label' => t('all_salaries')],
        ['value' => '1500', 'label' => '€1,500+'],
        ['value' => '2000', 'label' => '€2,000+'],
        ['value' => '2500', 'label' => '€2,500+'],
        ['value' => '3000', 'label' => '€3,000+'],
        ['value' => '3500', 'label' => '€3,500+'],
        ['value' => '4000', 'label' => '€4,000+'],
    ];
}

// Obsługa wyszukiwania
$search_results = [];
$where_conditions = ["status = 'active'"];
$params = [];

// Filtry
$filters = [
    'search' => $_GET['q'] ?? '',
    'country' => $_GET['country'] ?? '',
    'region' => $_GET['region'] ?? '',
    'location' => $_GET['location'] ?? '',
    'industry' => $_GET['industry'] ?? '',
    'job_role' => $_GET['job_role'] ?? '',
    'employment_type' => $_GET['employment_type'] ?? '',
    'salary_min' => $_GET['salary_min'] ?? '',
    'language' => $_GET['language'] ?? '',
    'remote' => $_GET['remote'] ?? '',
    'accommodation' => $_GET['accommodation'] ?? '0',
    'transport' => $_GET['transport'] ?? '0',
    'meals' => $_GET['meals'] ?? '0',
    'visa' => $_GET['visa'] ?? '0',
    'urgent' => $_GET['urgent'] ?? '0'
];

// WYSZUKIWANIE W TŁUMACZENIACH OGŁOSZEŃ - 11 JĘZYKÓW (wszystkie które masz w bazie)
if (!empty($filters['search'])) {
    $search_term = "%{$filters['search']}%";
    $where_conditions[] = "(title_pl LIKE ? OR title_nl LIKE ? OR title_en LIKE ? OR title_de LIKE ? OR title_cs LIKE ? OR title_ro LIKE ? OR 
                           title_bg LIKE ? OR title_hi LIKE ? OR title_hu LIKE ? OR title_ar LIKE ? OR title_uk LIKE ? OR
                           description_pl LIKE ? OR description_nl LIKE ? OR description_en LIKE ? OR description_de LIKE ? OR description_cs LIKE ? OR description_ro LIKE ? OR 
                           description_bg LIKE ? OR description_hi LIKE ? OR description_hu LIKE ? OR description_ar LIKE ? OR description_uk LIKE ? OR
                           requirements_pl LIKE ? OR requirements_nl LIKE ? OR requirements_en LIKE ? OR requirements_de LIKE ? OR requirements_cs LIKE ? OR requirements_ro LIKE ? OR
                           requirements_bg LIKE ? OR requirements_hi LIKE ? OR requirements_hu LIKE ? OR requirements_ar LIKE ? OR requirements_uk LIKE ?)";
    
    // 33 parametry (3 pola × 11 języków)
    for ($i = 0; $i < 33; $i++) {
        $params[] = $search_term;
    }
}

if (!empty($filters['country'])) {
    $where_conditions[] = "country_id = ?";
    $params[] = $filters['country'];
}

if (!empty($filters['region'])) {
    $where_conditions[] = "region = ?";
    $params[] = $filters['region'];
}

if (!empty($filters['location'])) {
    $where_conditions[] = "city = ?";
    $params[] = $filters['location'];
}

if (!empty($filters['industry'])) {
    $where_conditions[] = "industry_id = ?";
    $params[] = $filters['industry'];
}

if (!empty($filters['job_role'])) {
    // Obsługa: jeśli przekazano numeric id (dropdown) — użyj dokładnego dopasowania.
    // Jeśli przekazano tekst (np. użytkownik wpisał nazwę zawodu) — spróbuj znaleźć pasujące category_id po nazwie w bieżącym języku i użyj IN(...).
    $role_val = $filters['job_role'];
    if (is_numeric($role_val)) {
        $where_conditions[] = "category_id = ?";
        $params[] = (int)$role_val;
    } else {
        try {
            $like = "%{$role_val}%";
            // Szukamy po wszystkich kolumnach nazw (wszystkie języki dostępne w $available_languages)
            $name_clauses = [];
            $name_params = [];
            foreach ($available_languages as $lg) {
                $col = "name_" . $lg;
                $name_clauses[] = "$col LIKE ?";
                $name_params[] = $like;
            }
            $sql = "SELECT id FROM job_categories WHERE (" . implode(' OR ', $name_clauses) . ") LIMIT 50";
            $cat_stmt = $pdo->prepare($sql);
            $cat_stmt->execute($name_params);
            $cat_ids = $cat_stmt->fetchAll(PDO::FETCH_COLUMN, 0);
            if (!empty($cat_ids)) {
                $placeholders = implode(', ', array_fill(0, count($cat_ids), '?'));
                $where_conditions[] = "category_id IN ($placeholders)";
                foreach ($cat_ids as $cid) $params[] = $cid;
            } else {
                // brak dopasowań po nazwie => ignoruj filtr
            }
        } catch (PDOException $e) {
            // w razie błędu DB — ignoruj filtr
        }
    }
}

if (!empty($filters['employment_type'])) {
    $where_conditions[] = "employment_type = ?";
    $params[] = $filters['employment_type'];
}

if (!empty($filters['salary_min'])) {
    $where_conditions[] = "salary_min >= ?";
    $params[] = $filters['salary_min'];
}

if (!empty($filters['language'])) {
    $where_conditions[] = "language_requirements LIKE ?";
    $params[] = "%{$filters['language']}%";
}

if (!empty($filters['remote'])) {
    $where_conditions[] = "remote_option = ?";
    $params[] = $filters['remote'];
}

// Checkboxy benefitów
if ($filters['accommodation'] === '1') {
    $where_conditions[] = "accommodation_provided = 1";
}

if ($filters['transport'] === '1') {
    $where_conditions[] = "transport_provided = 1";
}

if ($filters['meals'] === '1') {
    $where_conditions[] = "meals_provided = 1";
}

if ($filters['visa'] === '1') {
    $where_conditions[] = "visa_assistance = 1";
}

if ($filters['urgent'] === '1') {
    $where_conditions[] = "urgent_hire = 1";
}

// PAGINACJA - pobierz WSZYSTKIE oferty z bazy (lub przefiltrowane)
$items_per_page = 12; // Zmienione z 8 na 12
$page = isset($_GET['page']) ? (int)$_GET['page'] : 1;
if ($page < 1) $page = 1;
$offset = ($page - 1) * $items_per_page;

// Najpierw pobierz całkowitą liczbę ofert
$count_sql = "SELECT COUNT(*) as total FROM job_offers jo WHERE " . implode(" AND ", $where_conditions);
try {
    $count_stmt = $pdo->prepare($count_sql);
    $count_stmt->execute($params);
    $total_count_result = $count_stmt->fetch(PDO::FETCH_ASSOC);
    $total_jobs = $total_count_result['total'];
} catch(PDOException $e) {
    $total_jobs = 0;
}

// Oblicz liczbę stron
$total_pages = $total_jobs > 0 ? ceil($total_jobs / $items_per_page) : 1;
if ($page > $total_pages && $total_pages > 0) {
    $page = $total_pages;
    $offset = ($page - 1) * $items_per_page;
}

// Pobierz oferty z paginacją
$sql = "SELECT 
            jo.*, 
            c.name_en as country_name,
            c.name_$current_lang as country_name_local,
            ind.name_$current_lang as industry_name,
            cat.name_$current_lang as category_name,
            emp.name_$current_lang as employment_type_name
        FROM job_offers jo
        LEFT JOIN countries c ON jo.country_id = c.id
        LEFT JOIN industries ind ON jo.industry_id = ind.id
        LEFT JOIN job_categories cat ON jo.category_id = cat.id
        LEFT JOIN employment_types emp ON jo.employment_type = emp.code
        WHERE " . implode(" AND ", $where_conditions) . " 
        ORDER BY jo.created_at DESC 
        LIMIT $items_per_page OFFSET $offset";

try {
    $stmt = $pdo->prepare($sql);
    $stmt->execute($params);
    $latest_jobs = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch(PDOException $e) {
    $latest_jobs = [];
}

// Jeśli brak ofert, wyświetl komunikat
if (empty($latest_jobs)) {
    $total_jobs = 0;
}

// AJAX endpoint: zwracaj fragment HTML listy ofert dla live-filter (action=jobs_list)
if (isset($_GET['ajax']) && $_GET['ajax'] == '1' && isset($_GET['action']) && $_GET['action'] === 'jobs_list') {
    header('Content-Type: text/html; charset=utf-8');
    if (!empty($latest_jobs)) {
        foreach ($latest_jobs as $job) {
            $title_field = 'title_' . $current_lang;
            $title = htmlspecialchars($job[$title_field] ?? $job['title_en'] ?? $job['title'] ?? '');
            $company = htmlspecialchars($job['employer_name'] ?? 'HR Consulting Partner');
            $city = htmlspecialchars($job['city'] ?? '');
            $country = htmlspecialchars($job['country_name_local'] ?? $job['country_name'] ?? '');
            $employment = htmlspecialchars($job['employment_type_name'] ?? $job['employment_type'] ?? '');
            $salary = $job['salary_min'] ? '€'.number_format($job['salary_min'],0) . '+' : '';
            $description_field = 'description_' . $current_lang;
            $description = strip_tags($job[$description_field] ?? $job['description_en'] ?? $job['description'] ?? '');
            $desc_short = strlen($description) > 200 ? substr($description,0,200) . '...' : $description;
            $job_id = $job['id'];
            // Apply links
            $whatsapp_number = '31657558110';
            $wa_link = 'https://wa.me/' . $whatsapp_number . '?text=' . rawurlencode('Hello, I am interested in job ID ' . $job_id . ' - ' . $title);
            $apply_link = 'application.php?job_id=' . $job_id;
            $mailto = 'mailto:?subject=' . rawurlencode('Application for job ' . $title) . '&body=' . rawurlencode('I am interested in job ID ' . $job_id . "\n\nPlease contact me.");

            echo "<article class=\"job-card\">";
            if ($job['urgent_hire']) echo "<span class=\"job-badge\"><i class=\"fas fa-bolt\"></i>".t('urgent')."</span>";
            echo "<div class=\"job-header\"><h3 class=\"job-title\">{$title}</h3><div class=\"job-company\">{$company}</div>";
            echo "<div class=\"job-meta\"><div class=\"meta-item\"><i class=\"fas fa-map-marker-alt\"></i><span>{$city}, {$country}</span></div><div class=\"meta-item\"><i class=\"fas fa-clock\"></i><span>{$employment}</span></div>";
            if ($salary) echo "<div class=\"meta-item\"><i class=\"fas fa-euro-sign\"></i><span>{$salary} / ".t('week')."</span></div>";
            echo "</div></div>";
            echo "<div class=\"job-content\"><p class=\"job-description\">" . htmlspecialchars($desc_short) . "</p></div>";
            echo "<div class=\"job-footer\">";
            echo "<a class=\"btn btn-primary\" href=\"{$apply_link}\"><i class=\"fas fa-paper-plane\"></i> " . t('apply_via_website') . "</a> ";
            echo "<a class=\"btn btn-secondary\" href=\"{$wa_link}\" target=\"_blank\"><i class=\"fab fa-whatsapp\"></i> " . t('apply_via_whatsapp') . "</a> ";
            echo "<a class=\"btn btn-secondary\" href=\"{$mailto}\"><i class=\"fas fa-envelope\"></i> " . t('apply_via_email') . "</a>";
            echo "</div></article>";
        }
    } else {
        echo "<div class=\"no-results\"><h3>😔 " . t('no_results_title') . "</h3><p>" . t('no_results_text') . "</p></div>";
    }
    // pagination info
    echo "<div class=\"pagination\">";
    echo "<div class=\"pagination-info\">" . t('page') . " {$page} " . t('of') . " {$total_pages}</div>";
    echo "</div>";
    exit;
}
?>
<!DOCTYPE html>
<html lang="<?php echo $current_lang; ?>" dir="<?php echo $current_lang == 'ar' ? 'rtl' : 'ltr'; ?>">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo t('website_title'); ?> | <?php echo t('nav_jobs'); ?></title>
    
    <!-- Meta Tags SEO -->
    <meta name="description" content="<?php echo t('hero_subtitle'); ?>">
    <meta name="keywords" content="praca Holandia, oferty pracy, zatrudnienie, HR Consulting Partner">
    
    <!-- Open Graph -->
    <meta property="og:title" content="<?php echo t('website_title'); ?> | <?php echo t('nav_jobs'); ?>">
    <meta property="og:description" content="<?php echo t('hero_subtitle'); ?>">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://job.hrconsultingpartner.nl/images/og-image.jpg">
    <meta property="og:url" content="https://job.hrconsultingpartner.nl/job_board.php">
    
    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="<?php echo t('website_title'); ?>">
    <meta name="twitter:description" content="<?php echo t('hero_subtitle'); ?>">
    
    <!-- Favicon -->
    <link rel="icon" href="/images/favicon.ico" type="image/x-icon">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <style>
        /* ===== VARIABLES ===== */
        :root {
            /* Nowa paleta kolorów */
            --primary: #0A3D62; /* Granatowy - główny kolor */
            --primary-dark: #08314f;
            --primary-light: #e6f2ff;
            --secondary: #3498DB; /* Błękitny - akcentujący */
            --accent: #E67E22; /* Pomarańczowy - CTA */
            --success: #27ae60;
            --warning: #f39c12;
            --danger: #e74c3c;
            --dark: #2C3E50; /* Grafit - teksty */
            --light: #FFFFFF; /* Biały - tło */
            --gray-100: #ECF0F1; /* Jasny szary - karty */
            --gray-200: #dfe6e9;
            --gray-300: #b2bec3;
            --gray-400: #95a5a6;
            --gray-500: #7f8c8d;
            --gray-600: #636e72;
            --gray-700: #2d3436;
            --gray-800: #1e272e;
            --gray-900: #0c2461;
            
            --shadow-sm: 0 1px 3px rgba(10, 61, 98, 0.12);
            --shadow: 0 4px 6px rgba(10, 61, 98, 0.1);
            --shadow-md: 0 6px 12px rgba(10, 61, 98, 0.15);
            --shadow-lg: 0 10px 25px rgba(10, 61, 98, 0.2);
            --shadow-xl: 0 20px 40px rgba(10, 61, 98, 0.25);
            
            --radius-sm: 6px;
            --radius: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
            --radius-xl: 24px;
            
            --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }
        
        /* ===== RESET & BASE STYLES ===== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html {
            scroll-behavior: smooth;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            color: var(--dark);
            background-color: var(--light);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            line-height: 1.3;
            color: var(--primary);
        }
        
        a {
            text-decoration: none;
            color: inherit;
            transition: var(--transition);
        }
        
        ul {
            list-style: none;
        }
        
        img {
            max-width: 100%;
            height: auto;
        }
        
        button, input, select, textarea {
            font-family: inherit;
            font-size: inherit;
        }
        
        .container {
            width: 100%;
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 1.5rem;
        }
        
        /* ===== HEADER & NAVIGATION ===== */
        .header {
            background: var(--light);
            box-shadow: var(--shadow);
            position: sticky;
            top: 0;
            z-index: 1000;
            transition: var(--transition);
            border-bottom: 3px solid var(--primary);
        }
        
        .header.scrolled {
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(10px);
        }
        
        .nav-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.75rem 0;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-shrink: 0;
        }
        
        /* USUNIĘTO: .logo-icon */
        
        .logo-text {
            font-size: 0.95rem; /* ZMIENIONE z 1.1rem */
            font-weight: 700;
            color: var(--primary);
            white-space: nowrap;
        }
        
        .logo-text span {
            font-size: 0.75rem; /* ZMIENIONE z 0.85rem */
            color: var(--gray-600);
            display: block;
            font-weight: 400;
            margin-top: 2px;
        }
        
        .nav-menu {
            display: flex;
            align-items: center;
            gap: 1.5rem;
            flex: 1;
            justify-content: flex-end;
        }
        
        .nav-links {
            display: flex;
            gap: 1.5rem;
            margin-right: 1rem;
        }
        
        .nav-link {
            font-weight: 500;
            color: var(--gray-700);
            padding: 0.5rem 0;
            position: relative;
            transition: var(--transition);
            font-size: 0.95rem;
            white-space: nowrap;
        }
        
        .nav-link:hover {
            color: var(--primary);
        }
        
        .nav-link.active {
            color: var(--primary);
            font-weight: 600;
        }
        
        .nav-link.active::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: var(--accent);
            border-radius: 2px;
        }
        
        /* Language Switcher in Navigation */
        .lang-switcher {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--gray-100);
            padding: 0.25rem;
            border-radius: var(--radius);
            border: 1px solid var(--gray-200);
        }
        
        .lang-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 32px;
            height: 32px;
            border-radius: var(--radius-sm);
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--gray-700);
            background: transparent;
            border: none;
            cursor: pointer;
            transition: var(--transition);
        }
        
        .lang-btn:hover {
            background: var(--gray-200);
            color: var(--primary);
            transform: translateY(-1px);
        }
        
        .lang-btn.active {
            background: var(--primary);
            color: white;
            box-shadow: var(--shadow-sm);
        }
        
        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            font-size: 1.5rem;
            color: var(--primary);
            cursor: pointer;
            padding: 0.5rem;
            border-radius: var(--radius);
            transition: var(--transition);
        }
        
        .mobile-menu-btn:hover {
            background: var(--gray-100);
        }
        
        /* ===== HERO SECTION ===== */
        .hero {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
            padding: 4rem 0;
            position: relative;
            overflow: hidden;
        }
        
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M0,0 L100,0 L100,100 Z" fill="white" opacity="0.05"/></svg>');
            background-size: cover;
        }
        
        .hero-content {
            position: relative;
            z-index: 1;
            text-align: center;
            max-width: 800px;
            margin: 0 auto;
        }
        
        .hero h1 {
            font-size: 2.75rem;
            margin-bottom: 1.25rem;
            color: white;
            line-height: 1.2;
        }
        
        .hero p {
            font-size: 1.125rem;
            margin-bottom: 2rem;
            opacity: 0.95;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .search-box {
            background: white;
            border-radius: var(--radius-lg);
            padding: 0.75rem;
            display: flex;
            gap: 0.75rem;
            box-shadow: var(--shadow-xl);
            max-width: 700px;
            margin: 0 auto;
        }
        
        .search-input {
            flex: 1;
            padding: 1rem 1.5rem;
            border: none;
            background: var(--gray-100);
            border-radius: var(--radius);
            font-size: 1rem;
            transition: var(--transition);
            color: var(--dark);
        }
        
        .search-input:focus {
            outline: none;
            background: white;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2);
        }
        
        .search-btn {
            padding: 1rem 2rem;
            background: var(--accent);
            color: white;
            border: none;
            border-radius: var(--radius);
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: var(--transition);
            white-space: nowrap;
        }
        
        .search-btn:hover {
            background: #d35400;
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }
        
        /* ===== FILTERS SECTION ===== */
        .filters-section {
            padding: 2.5rem 0;
            background: var(--gray-100);
            border-bottom: 1px solid var(--gray-200);
        }
        
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
        }
        
        .section-title {
            font-size: 1.5rem;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        
        .clear-filters {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--primary);
            font-weight: 500;
            background: none;
            border: none;
            cursor: pointer;
            transition: var(--transition);
            padding: 0.5rem 1rem;
            border-radius: var(--radius);
        }
        
        .clear-filters:hover {
            background: var(--gray-200);
            color: var(--primary-dark);
        }
        
        .filters-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.25rem;
        }
        
        .filter-group {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        
        .filter-label {
            font-size: 0.875rem;
            font-weight: 600;
            color: var(--gray-700);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .filter-select {
            padding: 0.875rem 1rem;
            border: 1px solid var(--gray-300);
            border-radius: var(--radius);
            background: white;
            font-size: 0.95rem;
            color: var(--dark);
            cursor: pointer;
            transition: var(--transition);
            appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23474b50' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 1rem center;
            background-size: 1rem;
        }
        
        .filter-select:focus {
            outline: none;
            border-color: var(--secondary);
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
        }
        
        /* ===== JOBS SECTION ===== */
        .jobs-section {
            padding: 3.5rem 0;
            background: var(--light);
        }
        
        .jobs-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2.5rem;
        }
        
        .jobs-title {
            font-size: 1.75rem;
            color: var(--primary);
        }
        
        .jobs-count {
            font-size: 1.125rem;
            color: var(--gray-600);
        }
        
        .jobs-count span {
            font-weight: 700;
            color: var(--accent);
        }
        
        .jobs-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 1.75rem;
        }
        
        /* ===== JOB CARD ===== */
        .job-card {
            background: var(--light);
            border-radius: var(--radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: var(--transition);
            border: 1px solid var(--gray-200);
            height: 100%;
            display: flex;
            flex-direction: column;
        }
        
        .job-card:hover {
            transform: translateY(-6px);
            box-shadow: var(--shadow-xl);
            border-color: var(--secondary);
        }
        
        .job-header {
            padding: 1.75rem 1.75rem 1rem;
            border-bottom: 1px solid var(--gray-200);
        }
        
        .job-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.375rem 0.75rem;
            background: var(--accent);
            color: white;
            border-radius: var(--radius);
            font-size: 0.75rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        
        .job-title {
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
            color: var(--primary);
            line-height: 1.4;
        }
        
        .job-company {
            color: var(--secondary);
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        
        .job-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .meta-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.875rem;
            color: var(--gray-600);
        }
        
        .meta-item i {
            color: var(--secondary);
        }
        
        .job-content {
            padding: 1.5rem 1.75rem;
            flex: 1;
        }
        
        .job-description {
            color: var(--gray-700);
            font-size: 0.95rem;
            line-height: 1.7;
            margin-bottom: 1.5rem;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
        
        .job-benefits {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
        }
        
        .benefit-tag {
            display: inline-flex;
            align-items: center;
            gap: 0.375rem;
            padding: 0.375rem 0.75rem;
            background: var(--gray-100);
            color: var(--gray-700);
            border-radius: var(--radius);
            font-size: 0.75rem;
            font-weight: 500;
            cursor: pointer;
            transition: var(--transition);
        }
        
        .benefit-tag:hover {
            background: var(--secondary);
            color: white;
        }
        
        .benefit-tag:hover i {
            color: white;
        }
        
        .benefit-tag.active {
            background: var(--accent);
            color: white;
        }
        
        .benefit-tag.active i {
            color: white;
        }
        
        .job-footer {
            padding: 1.5rem 1.75rem;
            border-top: 1px solid var(--gray-200);
            display: flex;
            gap: 1rem;
        }
        
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            padding: 0.75rem 1.5rem;
            border-radius: var(--radius);
            font-weight: 600;
            font-size: 0.95rem;
            cursor: pointer;
            transition: var(--transition);
            border: none;
            text-decoration: none;
        }
        
        .btn-primary {
            background: var(--secondary);
            color: white;
            flex: 1;
        }
        
        .btn-primary:hover {
            background: var(--primary);
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }
        
        .btn-secondary {
            background: transparent;
            color: var(--primary);
            border: 1px solid var(--primary);
            flex: 1;
        }
        
        .btn-secondary:hover {
            background: var(--primary);
            color: white;
        }
        
        .btn-apply {
            background: var(--accent);
            color: white;
            width: 100%;
            margin-top: 1rem;
            font-weight: 600;
        }
        
        .btn-apply:hover {
            background: #d35400;
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }
        
        /* ===== PAGINATION ===== */
        .pagination {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 0.5rem;
            margin-top: 3rem;
            flex-wrap: wrap;
        }
        
        .pagination-info {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
            justify-content: center;
            width: 100%;
            color: var(--gray-600);
            font-size: 0.9rem;
        }
        
        .pagination-controls {
            display: flex;
            gap: 0.5rem;
        }
        
        .pagination-link {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.5rem 1rem;
            background: var(--gray-100);
            color: var(--dark);
            border-radius: var(--radius);
            font-weight: 500;
            transition: var(--transition);
            text-decoration: none;
            min-width: 40px;
            border: 1px solid transparent;
        }
        
        .pagination-link:hover {
            background: var(--secondary);
            color: white;
            transform: translateY(-1px);
        }
        
        .pagination-link.active {
            background: var(--primary);
            color: white;
            font-weight: 600;
            border-color: var(--primary);
        }
        
        .pagination-link.prev,
        .pagination-link.next {
            background: var(--light);
            border: 1px solid var(--gray-300);
        }
        
        .pagination-link.prev:hover,
        .pagination-link.next:hover {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }
        
        .pagination-link.disabled {
            opacity: 0.5;
            cursor: not-allowed;
            pointer-events: none;
        }
        
        .pagination-link.disabled:hover {
            background: var(--gray-100);
            color: var(--dark);
            transform: none;
        }
        
        /* ===== STATS SECTION ===== */
        .stats-section {
            padding: 3.5rem 0;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            text-align: center;
        }
        
        .stat-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.75rem;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: 700;
            color: white;
            line-height: 1;
        }
        
        .stat-label {
            font-size: 1rem;
            color: var(--gray-200);
        }
        
        /* ===== FOOTER ===== */
        .footer {
            background: var(--primary);
            color: var(--gray-200);
            padding: 3.5rem 0 2rem;
        }
        
        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2.5rem;
            margin-bottom: 2.5rem;
        }
        
        .footer-col h3 {
            color: white;
            font-size: 1.25rem;
            margin-bottom: 1.5rem;
            position: relative;
            padding-bottom: 0.75rem;
        }
        
        .footer-col h3::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 40px;
            height: 2px;
            background: var(--accent);
        }
        
        .footer-links li {
            margin-bottom: 0.75rem;
        }
        
        .footer-links a {
            color: var(--gray-300);
            transition: var(--transition);
        }
        
        .footer-links a:hover {
            color: white;
            padding-left: 0.5rem;
        }
        
        .social-links {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
        }
        
        .social-link {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            transition: var(--transition);
        }
        
        .social-link:hover {
            background: var(--accent);
            transform: translateY(-3px);
        }
        
        .footer-bottom {
            padding-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            text-align: center;
            color: var(--gray-300);
            font-size: 0.875rem;
        }
        
        /* ===== RTL SUPPORT ===== */
        [dir="rtl"] .logo-text {
            text-align: right;
        }
        
        [dir="rtl"] .footer-col h3::after {
            left: auto;
            right: 0;
        }
        
        [dir="rtl"] .footer-links a:hover {
            padding-left: 0;
            padding-right: 0.5rem;
        }
        
        [dir="rtl"] .filter-select {
            background-position: left 1rem center;
        }
        
        /* ===== RESPONSIVE DESIGN ===== */
        @media (max-width: 1200px) {
            .logo-text {
                font-size: 0.85rem;
            }
            
            .logo-text span {
                font-size: 0.65rem;
            }
            
            .nav-links {
                gap: 1rem;
            }
            
            .nav-link {
                font-size: 0.9rem;
            }
        }
        
        @media (max-width: 1100px) {
            .nav-menu {
                gap: 1rem;
            }
            
            .filters-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        
        @media (max-width: 1024px) {
            .hero h1 {
                font-size: 2.25rem;
            }
            
            .nav-menu {
                position: fixed;
                top: 70px;
                left: -100%;
                width: 100%;
                background: white;
                flex-direction: column;
                align-items: flex-start;
                padding: 2rem;
                box-shadow: var(--shadow-lg);
                transition: var(--transition);
                z-index: 999;
                gap: 1rem;
            }
            
            .nav-menu.active {
                left: 0;
            }
            
            .nav-links {
                flex-direction: column;
                width: 100%;
                gap: 0;
                margin-right: 0;
            }
            
            .nav-link {
                padding: 1rem 0;
                width: 100%;
                border-bottom: 1px solid var(--gray-200);
            }
            
            .lang-switcher {
                margin-top: 1rem;
                width: 100%;
                justify-content: center;
            }
            
            .mobile-menu-btn {
                display: block;
            }
            
            .filters-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .jobs-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            
            .hero p {
                font-size: 1rem;
            }
            
            .search-box {
                flex-direction: column;
            }
            
            .search-btn {
                width: 100%;
                justify-content: center;
            }
            
            .filters-grid {
                grid-template-columns: 1fr;
            }
            
            .jobs-grid {
                grid-template-columns: 1fr;
            }
            
            .section-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 1rem;
            }
            
            .job-footer {
                flex-direction: column;
            }
            
            .btn {
                width: 100%;
            }
            
            .logo-text {
                font-size: 0.9rem;
            }
            
            .logo-text span {
                font-size: 0.7rem;
            }
        }
        
        @media (max-width: 640px) {
            .container {
                padding: 0 1rem;
            }
            
            .hero {
                padding: 3rem 0;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
                gap: 1.5rem;
            }
            
            .stat-number {
                font-size: 2rem;
            }
        }
        
        @media (max-width: 480px) {
            .hero h1 {
                font-size: 1.75rem;
            }
            
            .jobs-title {
                font-size: 1.5rem;
            }
            
            .section-title {
                font-size: 1.25rem;
            }
        }
        
        /* ===== UTILITY CLASSES ===== */
        .text-center {
            text-align: center;
        }
        
        .mb-1 { margin-bottom: 0.5rem; }
        .mb-2 { margin-bottom: 1rem; }
        .mb-3 { margin-bottom: 1.5rem; }
        .mb-4 { margin-bottom: 2rem; }
        .mb-5 { margin-bottom: 3rem; }
        
        .mt-1 { margin-top: 0.5rem; }
        .mt-2 { margin-top: 1rem; }
        .mt-3 { margin-top: 1.5rem; }
        .mt-4 { margin-top: 2rem; }
        .mt-5 { margin-top: 3rem; }
        
        .flex {
            display: flex;
        }
        
        .items-center {
            align-items: center;
        }
        
        .justify-between {
            justify-content: space-between;
        }
        
        .gap-1 { gap: 0.5rem; }
        .gap-2 { gap: 1rem; }
        .gap-3 { gap: 1.5rem; }
        .gap-4 { gap: 2rem; }
        .gap-5 { gap: 3rem; }
        
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Header & Navigation -->
    <header class="header" id="header">
        <div class="container">
            <nav class="nav-container">
                <a href="?" class="logo">
                    <!-- USUNIĘTO: <div class="logo-icon">HR</div> -->
                    <div class="logo-text">
                        HR Consulting Partner
                        <span><?php echo t('nav_jobs'); ?></span>
                    </div>
                </a>
                
                <div class="nav-menu" id="navMenu">
                    <ul class="nav-links">
                        <li><a href="index.html" class="nav-link"><?php echo t('nav_home'); ?></a></li>
                        <li><a href="candidates.php" class="nav-link"><?php echo t('nav_cv'); ?></a></li>
                        <li><a href="job_board.php" class="nav-link active"><?php echo t('nav_jobs'); ?></a></li>
                        <li><a href="firma.html" class="nav-link"><?php echo t('nav_companies'); ?></a></li>
                        <li><a href="Overons.html" class="nav-link"><?php echo t('nav_about'); ?></a></li>
                        <li><a href="contactus2.html" class="nav-link"><?php echo t('nav_contact'); ?></a></li>
                        <li><a href="ai-chat.html" class="nav-link"><?php echo t('nav_ai'); ?></a></li>
                    </ul>
                    
                    <div class="lang-switcher">
                        <?php foreach ($available_languages as $lang): ?>
                            <a href="<?php echo getLanguageUrl($lang); ?>" 
                               class="lang-btn <?php echo $current_lang == $lang ? 'active' : ''; ?>"
                               title="<?php echo strtoupper($lang); ?>">
                                <?php echo strtoupper(substr($lang, 0, 2)); ?>
                            </a>
                        <?php endforeach; ?>
                    </div>
                </div>
                
                <button class="mobile-menu-btn" id="mobileMenuBtn">
                    <i class="fas fa-bars"></i>
                </button>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <h1><?php echo t('hero_title'); ?></h1>
                <p><?php echo t('hero_subtitle'); ?></p>
                
                <form method="GET" action="" class="search-box">
                    <input type="hidden" name="lang" value="<?php echo $current_lang; ?>">
                    <input type="text" 
                           name="q" 
                           class="search-input" 
                           placeholder="<?php echo t('search_placeholder'); ?>"
                           value="<?php echo htmlspecialchars($filters['search']); ?>">
                    <button type="submit" class="search-btn">
                        <i class="fas fa-search"></i>
                        <?php echo t('btn_search'); ?>
                    </button>
                </form>
            </div>
        </div>
    </section>

    <!-- Filters Section -->
    <section class="filters-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">
                    <i class="fas fa-filter"></i>
                    <?php echo t('filters_title'); ?>
                </h2>
                <button type="button" class="clear-filters" onclick="clearAllFilters()">
                    <i class="fas fa-times"></i>
                    <?php echo t('btn_clear'); ?>
                </button>
            </div>
            
            <form method="GET" id="filterForm" class="filters-grid">
                <input type="hidden" name="lang" value="<?php echo $current_lang; ?>">
                <input type="hidden" name="q" value="<?php echo htmlspecialchars($filters['search']); ?>">
                <input type="hidden" name="accommodation" id="accommodationInput" value="<?php echo $filters['accommodation']; ?>">
                <input type="hidden" name="transport" id="transportInput" value="<?php echo $filters['transport']; ?>">
                <input type="hidden" name="meals" id="mealsInput" value="<?php echo $filters['meals']; ?>">
                <input type="hidden" name="visa" id="visaInput" value="<?php echo $filters['visa']; ?>">
                <input type="hidden" name="urgent" id="urgentInput" value="<?php echo $filters['urgent']; ?>">
                
                <!-- Country Filter -->
                <div class="filter-group">
                    <label class="filter-label">
                        <i class="fas fa-globe-europe"></i>
                        <?php echo t('filter_country'); ?>
                    </label>
                    <select name="country" class="filter-select" onchange="this.form.submit()">
                        <option value=""><?php echo t('all_countries'); ?></option>
                        <?php foreach ($all_countries as $country): ?>
                            <option value="<?php echo $country['id']; ?>" 
                                <?php echo $filters['country'] == $country['id'] ? 'selected' : ''; ?>>
                                <?php echo htmlspecialchars($country["name_$current_lang"] ?? $country['name_en']); ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>
                
                <!-- City Filter -->
                <div class="filter-group">
                    <label class="filter-label">
                        <i class="fas fa-map-marker-alt"></i>
                        <?php echo t('filter_location'); ?>
                    </label>
                    <select name="location" class="filter-select" onchange="this.form.submit()">
                        <option value=""><?php echo t('all_cities'); ?></option>
                        <?php foreach ($dutch_cities as $city): ?>
                            <option value="<?php echo htmlspecialchars($city); ?>"
                                <?php echo $filters['location'] == $city ? 'selected' : ''; ?>>
                                <?php echo htmlspecialchars($city); ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>
                
                <!-- Industry Filter -->
                <div class="filter-group">
                    <label class="filter-label">
                        <i class="fas fa-industry"></i>
                        <?php echo t('filter_industry'); ?>
                    </label>
                    <select name="industry" class="filter-select" onchange="this.form.submit()">
                        <option value=""><?php echo t('all_industries'); ?></option>
                        <?php foreach ($industries as $industry): ?>
                            <option value="<?php echo $industry['id']; ?>"
                                <?php echo $filters['industry'] == $industry['id'] ? 'selected' : ''; ?>>
                                <?php echo htmlspecialchars($industry['name']); ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>
                
                <!-- Job Category Filter -->
                <div class="filter-group">
                    <label class="filter-label">
                        <i class="fas fa-briefcase"></i>
                        <?php echo t('filter_role'); ?>
                    </label>
                    <!-- Autocomplete input for job role: supports typing in any language and selecting a suggestion -->
                    <input type="text" id="jobRoleInput" class="filter-select" placeholder="<?php echo t('filter_role'); ?>" value="<?php echo htmlspecialchars(\
                        // show selected label if numeric id provided
                        (is_numeric($filters['job_role']) ? (function() use ($job_categories, $filters) {
                            foreach ($job_categories as $c) { if ($c['id'] == $filters['job_role']) return $c['name']; } return '';
                        })() : $filters['job_role'])
                    ); ?>">
                    <input type="hidden" name="job_role" id="jobRoleHidden" value="<?php echo htmlspecialchars($filters['job_role']); ?>">
                    <div id="jobRoleSuggestions" class="suggestions" style="display:none; position:relative;"></div>
                </div>
                
                <!-- Employment Type Filter -->
                <div class="filter-group">
                    <label class="filter-label">
                        <i class="fas fa-clock"></i>
                        <?php echo t('filter_type'); ?>
                    </label>
                    <select name="employment_type" class="filter-select" onchange="this.form.submit()">
                        <option value=""><?php echo t('all_types'); ?></option>
                        <?php foreach ($contract_types as $contract): ?>
                            <option value="<?php echo $contract['code']; ?>"
                                <?php echo $filters['employment_type'] == $contract['code'] ? 'selected' : ''; ?>>
                                <?php echo htmlspecialchars($contract['name']); ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>
                
                <!-- Salary Filter -->
                <div class="filter-group">
                    <label class="filter-label">
                        <i class="fas fa-euro-sign"></i>
                        <?php echo t('filter_salary'); ?>
                    </label>
                    <select name="salary_min" class="filter-select" onchange="this.form.submit()">
                        <?php foreach ($salary_ranges as $range): ?>
                            <option value="<?php echo $range['value']; ?>" 
                                <?php echo $filters['salary_min'] == $range['value'] ? 'selected' : ''; ?>>
                                <?php echo htmlspecialchars($range['label']); ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>
                
                <!-- Language Requirements -->
                <div class="filter-group">
                    <label class="filter-label">
                        <i class="fas fa-language"></i>
                        <?php echo t('filter_language'); ?>
                    </label>
                    <select name="language" class="filter-select" onchange="this.form.submit()">
                        <option value=""><?php echo t('all_languages'); ?></option>
                        <?php foreach ($language_requirements as $language): ?>
                            <option value="<?php echo $language['code']; ?>"
                                <?php echo $filters['language'] == $language['code'] ? 'selected' : ''; ?>>
                                <?php echo htmlspecialchars($language['name']); ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>
                
                <!-- Remote Work -->
                <div class="filter-group">
                    <label class="filter-label">
                        <i class="fas fa-home"></i>
                        <?php echo t('filter_remote'); ?>
                    </label>
                    <select name="remote" class="filter-select" onchange="this.form.submit()">
                        <option value=""><?php echo t('all_remote'); ?></option>
                        <option value="full" <?php echo $filters['remote'] == 'full' ? 'selected' : ''; ?>>
                            <?php echo t('remote_option_full'); ?>
                        </option>
                        <option value="partial" <?php echo $filters['remote'] == 'partial' ? 'selected' : ''; ?>>
                            <?php echo t('remote_option_partial'); ?>
                        </option>
                        <option value="none" <?php echo $filters['remote'] == 'none' ? 'selected' : ''; ?>>
                            <?php echo t('remote_option_none'); ?>
                        </option>
                    </select>
                </div>
                
                <!-- Region Filter -->
                <div class="filter-group">
                    <label class="filter-label">
                        <i class="fas fa-map"></i>
                        <?php echo t('filter_region'); ?>
                    </label>
                    <select name="region" class="filter-select" onchange="this.form.submit()">
                        <option value=""><?php echo t('all_regions'); ?></option>
                        <?php foreach ($regions as $region): ?>
                            <option value="<?php echo htmlspecialchars($region); ?>"
                                <?php echo $filters['region'] == $region ? 'selected' : ''; ?>>
                                <?php echo htmlspecialchars($region); ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>
            </form>
        </div>
    </section>

    <!-- Jobs Section -->
    <section class="jobs-section">
        <div class="container">
            <div class="jobs-header">
                <h2 class="jobs-title"><?php echo t('recent_jobs'); ?></h2>
                <div class="jobs-count">
                    <?php echo t('found'); ?> <span><?php echo $total_jobs; ?></span> <?php echo t('offers'); ?>
                    <?php if ($total_pages > 1): ?>
                        <span style="font-size: 0.9em; color: var(--gray-500); margin-left: 10px;">
                            (<?php echo t('page'); ?> <?php echo $page; ?> <?php echo t('of'); ?> <?php echo $total_pages; ?>)
                        </span>
                    <?php endif; ?>
                </div>
            </div>
            
            <div id="jobsContainer">
            <?php if (!empty($latest_jobs)): ?>
                <div class="jobs-grid">
                    <?php foreach ($latest_jobs as $job): ?>
                        <article class="job-card">
                            <div class="job-header">
                                <?php if ($job['urgent_hire']): ?>
                                    <span class="job-badge">
                                        <i class="fas fa-bolt"></i>
                                        <?php echo t('urgent'); ?>
                                    </span>
                                <?php endif; ?>
                                
                                <h3 class="job-title">
                                    <?php 
                                    $title_field = 'title_' . $current_lang;
                                    echo htmlspecialchars($job[$title_field] ?? $job['title_en'] ?? $job['title'] ?? '');
                                    ?>
                                </h3>
                                
                                <div class="job-company">
                                    <?php echo htmlspecialchars($job['employer_name'] ?? 'HR Consulting Partner'); ?>
                                </div>
                                
                                <div class="job-meta">
                                    <div class="meta-item">
                                        <i class="fas fa-map-marker-alt"></i>
                                        <span>
                                            <?php echo htmlspecialchars($job['city'] ?? ''); ?>, 
                                            <?php echo htmlspecialchars($job['country_name_local'] ?? $job['country_name'] ?? ''); ?>
                                        </span>
                                    </div>
                                    <div class="meta-item">
                                        <i class="fas fa-clock"></i>
                                        <span><?php echo htmlspecialchars($job['employment_type_name'] ?? $job['employment_type'] ?? ''); ?></span>
                                    </div>
                                    <?php if ($job['salary_min']): ?>
                                    <div class="meta-item">
                                        <i class="fas fa-euro-sign"></i>
                                        <span>€<?php echo number_format($job['salary_min'], 0); ?>+ / <?php echo t('week'); ?></span>
                                    </div>
                                    <?php endif; ?>
                                </div>
                            </div>
                            
                            <div class="job-content">
                                <p class="job-description">
                                    <?php 
                                    $description_field = 'description_' . $current_lang;
                                    $description = strip_tags($job[$description_field] ?? $job['description_en'] ?? $job['description'] ?? '');
                                    echo strlen($description) > 200 ? substr($description, 0, 200) . '...' : $description;
                                    ?>
                                </p>
                                
                                <div class="job-benefits">
                                    <?php if ($job['accommodation_provided']): ?>
                                        <span class="benefit-tag <?php echo $filters['accommodation'] == '1' ? 'active' : ''; ?>" 
                                              onclick="toggleBenefitFilter('accommodation', this)">
                                            <i class="fas fa-home"></i>
                                            <?php echo t('accommodation'); ?>
                                        </span>
                                    <?php endif; ?>
                                    <?php if ($job['transport_provided']): ?>
                                        <span class="benefit-tag <?php echo $filters['transport'] == '1' ? 'active' : ''; ?>" 
                                              onclick="toggleBenefitFilter('transport', this)">
                                            <i class="fas fa-car"></i>
                                            <?php echo t('transport'); ?>
                                        </span>
                                    <?php endif; ?>
                                    <?php if ($job['meals_provided']): ?>
                                        <span class="benefit-tag <?php echo $filters['meals'] == '1' ? 'active' : ''; ?>" 
                                              onclick="toggleBenefitFilter('meals', this)">
                                            <i class="fas fa-utensils"></i>
                                            <?php echo t('meals'); ?>
                                        </span>
                                    <?php endif; ?>
                                    <?php if ($job['visa_assistance']): ?>
                                        <span class="benefit-tag <?php echo $filters['visa'] == '1' ? 'active' : ''; ?>" 
                                              onclick="toggleBenefitFilter('visa', this)">
                                            <i class="fas fa-passport"></i>
                                            <?php echo t('visa'); ?>
                                        </span>
                                    <?php endif; ?>
                                </div>
                            </div>
                            
                            <div class="job-footer">
                                <button class="btn btn-secondary" onclick="saveJob(<?php echo $job['id']; ?>)">
                                    <i class="far fa-bookmark"></i>
                                    <?php echo t('btn_save'); ?>
                                </button>
                                <a href="job_details.php?id=<?php echo $job['id']; ?>&lang=<?php echo $current_lang; ?>" 
                                   class="btn btn-primary">
                                    <i class="fas fa-eye"></i>
                                    <?php echo t('btn_details'); ?>
                                </a>
                            </div>
                            
                            <div class="apply-links">
                                <a class="btn btn-primary" href="application.php?job_id=<?php echo $job['id']; ?>">
                                    <i class="fas fa-paper-plane"></i>
                                    <?php echo t('apply_via_website'); ?>
                                </a>
                                <a class="btn btn-secondary" target="_blank" href="https://wa.me/31657558110?text=<?php echo rawurlencode('Hello,%20I%20am%20interested%20in%20job%20ID%20' . $job['id'] . '%20-%20' . ($job['title_' . $current_lang] ?? $job['title_en'] ?? $job['title'] ?? '')); ?>">
                                    <i class="fab fa-whatsapp"></i>
                                    <?php echo t('apply_via_whatsapp'); ?>
                                </a>
                                <a class="btn btn-secondary" href="mailto:?subject=<?php echo rawurlencode('Application%20for%20job%20' . ($job['title_' . $current_lang] ?? $job['title_en'] ?? $job['title'] ?? '')); ?>&body=<?php echo rawurlencode('I%20am%20interested%20in%20job%20ID%20' . $job['id']); ?>">
                                    <i class="fas fa-envelope"></i>
                                    <?php echo t('apply_via_email'); ?>
                                </a>
                            </div>
                        </article>
                    <?php endforeach; ?>
                </div>
                
                <!-- Paginacja -->
                <?php if ($total_pages > 1): ?>
                    <div class="pagination">
                        <div class="pagination-info">
                            <span><?php echo t('page'); ?> <?php echo $page; ?> <?php echo t('of'); ?> <?php echo $total_pages; ?></span>
                            <span><?php echo $total_jobs; ?> <?php echo t('offers'); ?></span>
                        </div>
                        
                        <div class="pagination-controls">
                            <?php if ($page > 1): ?>
                                <a href="?<?php echo http_build_query(array_merge($_GET, ['page' => $page - 1])); ?>" class="pagination-link prev">
                                    <i class="fas fa-chevron-left"></i> <?php echo t('prev'); ?>
                                </a>
                            <?php else: ?>
                                <span class="pagination-link prev disabled">
                                    <i class="fas fa-chevron-left"></i> <?php echo t('prev'); ?>
                                </span>
                            <?php endif; ?>
                            
                            <?php
                            // Pokazuj maksymalnie 5 numerów stron
                            $start_page = max(1, $page - 2);
                            $end_page = min($total_pages, $start_page + 4);
                            $start_page = max(1, $end_page - 4);
                            
                            for ($i = $start_page; $i <= $end_page; $i++):
                            ?>
                                <?php if ($i == $page): ?>
                                    <span class="pagination-link active"><?php echo $i; ?></span>
                                <?php else: ?>
                                    <a href="?<?php echo http_build_query(array_merge($_GET, ['page' => $i])); ?>" class="pagination-link"><?php echo $i; ?></a>
                                <?php endif; ?>
                            <?php endfor; ?>
                            
                            <?php if ($page < $total_pages): ?>
                                <a href="?<?php echo http_build_query(array_merge($_GET, ['page' => $page + 1])); ?>" class="pagination-link next">
                                    <?php echo t('next'); ?> <i class="fas fa-chevron-right"></i>
                                </a>
                            <?php else: ?>
                                <span class="pagination-link next disabled">
                                    <?php echo t('next'); ?> <i class="fas fa-chevron-right"></i>
                                </span>
                            <?php endif; ?>
                        </div>
                    </div>
                <?php endif; ?>
                
            <?php else: ?>
                <div class="text-center">
                    <h3 class="mb-2"><?php echo t('no_results_title'); ?></h3>
                    <p class="mb-4"><?php echo t('no_results_text'); ?></p>
                    <a href="?lang=<?php echo $current_lang; ?>" class="btn btn-primary">
                        <i class="fas fa-redo"></i>
                        <?php echo t('btn_clear'); ?>
                    </a>
                </div>
            <?php endif; ?>
            </div>
        </div>
    </section>

    <!-- Stats Section -->
    <section class="stats-section">
        <div class="container">
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-number">500+</div>
                    <div class="stat-label">Ofert pracy</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">100+</div>
                    <div class="stat-label">Pracodawców</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">50+</div>
                    <div class="stat-label">Miast</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">24h</div>
                    <div class="stat-label">Szybka aplikacja</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h3>HR Consulting Partner</h3>
                    <p>Łączymy talenty z najlepszymi pracodawcami w Europie. Specjalizujemy się w rekrutacji międzynarodowej.</p>
                    <div class="social-links">
                        <a href="#" class="social-link"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="social-link"><i class="fab fa-linkedin-in"></i></a>
                        <a href="#" class="social-link"><i class="fab fa-twitter"></i></a>
                        <a href="#" class="social-link"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
                
                <div class="footer-col">
                    <h3><?php echo t('nav_jobs'); ?></h3>
                    <ul class="footer-links">
                        <li><a href="?country=1&lang=<?php echo $current_lang; ?>">Praca w Holandii</a></li>
                        <li><a href="?country=2&lang=<?php echo $current_lang; ?>">Praca w Niemczech</a></li>
                        <li><a href="?country=3&lang=<?php echo $current_lang; ?>">Praca w Belgii</a></li>
                        <li><a href="?remote=full&lang=<?php echo $current_lang; ?>">Praca zdalna</a></li>
                        <li><a href="?employment_type=seasonal&lang=<?php echo $current_lang; ?>">Praca sezonowa</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h3><?php echo t('nav_about'); ?></h3>
                    <ul class="footer-links">
                        <li><a href="Overons.html?lang=<?php echo $current_lang; ?>"><?php echo t('nav_about'); ?></a></li>
                        <li><a href="contactus2.html?lang=<?php echo $current_lang; ?>"><?php echo t('nav_contact'); ?></a></li>
                        <li><a href="#">FAQ</a></li>
                        <li><a href="#">Blog</a></li>
                        <li><a href="#">Kariera</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h3><?php echo t('nav_contact'); ?></h3>
                    <ul class="footer-links">
                        <li><i class="fas fa-envelope"></i> info@hrconsultingpartner.nl</li>
                        <li><i class="fas fa-phone"></i> +31 657 558 110</li>
                        <li><i class="fas fa-map-marker-alt"></i> Holandia</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2025 HR Consulting Partner. Wszystkie prawa zastrzeżone.</p>
            </div>
        </div>
    </footer>

    <script>
        // Mobile Menu Toggle
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const navMenu = document.getElementById('navMenu');
        
        mobileMenuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            mobileMenuBtn.innerHTML = navMenu.classList.contains('active') 
                ? '<i class="fas fa-times"></i>' 
                : '<i class="fas fa-bars"></i>';
        });
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navMenu.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                navMenu.classList.remove('active');
                mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
        
        // Header scroll effect
        const header = document.getElementById('header');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
        
        // Clear all filters
        function clearAllFilters() {
            window.location.href = '?lang=<?php echo $current_lang; ?>';
        }
        
        // Save job to localStorage
        function saveJob(jobId) {
            let savedJobs = JSON.parse(localStorage.getItem('savedJobs')) || [];
            
            if (!savedJobs.includes(jobId)) {
                savedJobs.push(jobId);
                localStorage.setItem('savedJobs', JSON.stringify(savedJobs));
                
                // Show success message
                showNotification('Oferta została zapisana!', 'success');
            } else {
                showNotification('Ta oferta jest już zapisana.', 'info');
            }
        }
        
        // Apply modal
        function showApplyModal(jobId, jobTitle) {
            // In a real implementation, this would show a modal
            // For now, redirect to contact page
            window.location.href = 'contactus2.html?job_id=' + jobId + '&job_title=' + encodeURIComponent(jobTitle) + '&lang=<?php echo $current_lang; ?>';
        }
        
        // Toggle benefit filters
        function toggleBenefitFilter(benefit, element) {
            const input = document.getElementById(benefit + 'Input');
            const currentValue = input.value;
            const newValue = currentValue === '1' ? '0' : '1';
            
            input.value = newValue;
            
            // Toggle active class
            if (newValue === '1') {
                element.classList.add('active');
            } else {
                element.classList.remove('active');
            }
            
            // Submit form
            document.getElementById('filterForm').submit();
        }
        
        // Notification function
        function showNotification(message, type = 'info') {
            // Create notification element
            const notification = document.createElement('div');
            notification.className = `notification notification-${type}`;
            notification.innerHTML = `
                <div class="notification-content">
                    <i class="fas fa-${type === 'success' ? 'check-circle' : 'info-circle'}"></i>
                    <span>${message}</span>
                </div>
                <button class="notification-close" onclick="this.parentElement.remove()">
                    <i class="fas fa-times"></i>
                </button>
            `;
            
            // Add styles
            notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: ${type === 'success' ? '#27ae60' : '#3498db'};
                color: white;
                padding: 1rem 1.5rem;
                border-radius: 8px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 1rem;
                z-index: 9999;
                animation: slideIn 0.3s ease;
                max-width: 400px;
            `;
            
            // Add to body
            document.body.appendChild(notification);
            
            // Auto remove after 5 seconds
            setTimeout(() => {
                if (notification.parentElement) {
                    notification.remove();
                }
            }, 5000);
        }
        
        // Add CSS animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideIn {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            
            .notification-content {
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }
            
            .notification-close {
                background: none;
                border: none;
                color: white;
                cursor: pointer;
                padding: 0.25rem;
                border-radius: 0.25rem;
                transition: background 0.3s;
            }
            
            .notification-close:hover {
                background: rgba(255, 255, 255, 0.1);
            }
        `;
        document.head.appendChild(style);
        
        // Initialize saved jobs
        document.addEventListener('DOMContentLoaded', () => {
            const savedJobs = JSON.parse(localStorage.getItem('savedJobs')) || [];
            console.log('Zapisane oferty:', savedJobs);
        });
    </script>
    <script>
        // Autocomplete for job role
        (function(){
            const input = document.getElementById('jobRoleInput');
            const hidden = document.getElementById('jobRoleHidden');
            const sugg = document.getElementById('jobRoleSuggestions');
            let debounceTimer = null;

            function clearSuggestions(){
                sugg.style.display = 'none';
                sugg.innerHTML = '';
            }

            function renderSuggestions(items){
                sugg.innerHTML = '';
                if (!items.length) { clearSuggestions(); return; }
                const ul = document.createElement('ul');
                ul.style.listStyle='none'; ul.style.margin='0'; ul.style.padding='0'; ul.style.position='absolute'; ul.style.zIndex='1000'; ul.style.background='white'; ul.style.border='1px solid #ddd'; ul.style.width = input.offsetWidth + 'px';
                items.forEach(it => {
                    const li = document.createElement('li');
                    li.textContent = it.label;
                    li.style.padding = '8px 10px';
                    li.style.cursor = 'pointer';
                    li.addEventListener('click', () => {
                        // set hidden id and visible label, then fetch results via AJAX
                        hidden.value = it.id;
                        input.value = it.label;
                        clearSuggestions();
                        fetchJobs(1);
                    });
                    ul.appendChild(li);
                });
                sugg.appendChild(ul);
                sugg.style.display = 'block';
            }

            input.addEventListener('input', (e) => {
                const q = e.target.value.trim();
                // clear hidden id when typing
                hidden.value = q;
                if (debounceTimer) clearTimeout(debounceTimer);
                if (!q) { clearSuggestions(); return; }
                debounceTimer = setTimeout(() => {
                    fetch(window.location.pathname + '?' + new URLSearchParams({ajax:1, action:'role_suggest', q: q}))
                        .then(r => r.json())
                        .then(data => renderSuggestions(data))
                        .catch(() => clearSuggestions());
                }, 250);
            });

            document.addEventListener('click', (ev) => {
                if (!sugg.contains(ev.target) && ev.target !== input) clearSuggestions();
            });
        })();

        // Live filtering: serialize form and fetch jobs fragment
        function serializeForm(form) {
            const data = new URLSearchParams();
            for (const el of form.elements) {
                if (!el.name) continue;
                if ((el.type === 'checkbox' || el.type === 'radio') && !el.checked) continue;
                data.append(el.name, el.value);
            }
            return data;
        }

        let liveTimer = null;
        function fetchJobs(page) {
            const form = document.getElementById('filterForm');
            const params = serializeForm(form);
            if (page) params.set('page', page);
            params.set('ajax', '1');
            params.set('action', 'jobs_list');
            const url = window.location.pathname + '?' + params.toString();
            const container = document.getElementById('jobsContainer');
            fetch(url)
                .then(r => r.text())
                .then(html => {
                    if (container) container.innerHTML = html;
                    attachPaginationHandlers();
                })
                .catch(err => console.error('Fetch jobs error', err));
        }

        function attachPaginationHandlers(){
            document.querySelectorAll('.pagination-link').forEach(a => {
                if (a._attached) return; a._attached = true;
                a.addEventListener('click', function(e){
                    e.preventDefault();
                    const q = new URL(this.href, window.location.href).searchParams.get('page');
                    fetchJobs(q || 1);
                });
            });
        }

        // Debounced form input handling
        document.getElementById('filterForm').addEventListener('input', function(e){
            if (liveTimer) clearTimeout(liveTimer);
            liveTimer = setTimeout(()=> fetchJobs(1), 300);
        });

        // Intercept form submit to use AJAX
        document.getElementById('filterForm').addEventListener('submit', function(e){
            e.preventDefault();
            fetchJobs(1);
        });

        // Attach handlers for initial pagination links
        attachPaginationHandlers();
    </script>
</body>
</html>