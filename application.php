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

// Ustawienia
$admin_email = "beata@hrconsultingpartner.nl";
$admin_phone = "0657558110";
$site_name = "HR Consulting Partner - Job Board";

// Języki
$available_languages = ['pl', 'nl', 'en', 'de', 'cs', 'ro', 'bg', 'hi', 'hu', 'ar', 'uk'];
$default_language = 'pl';

if (isset($_GET['lang']) && in_array($_GET['lang'], $available_languages)) {
    $_SESSION['lang'] = $_GET['lang'];
} elseif (!isset($_SESSION['lang'])) {
    $_SESSION['lang'] = $default_language;
}

$current_lang = $_SESSION['lang'];

// Tłumaczenia - podstawowe
$translations = [
    'pl' => [
        'page_title' => 'Aplikuj na stanowisko',
        'job_title' => 'Stanowisko',
        'your_name' => 'Twoje imię i nazwisko',
        'your_email' => 'Twój e-mail',
        'your_phone' => 'Twój telefon',
        'your_message' => 'Wiadomość (opcjonalnie)',
        'btn_send' => 'Wyślij aplikację',
        'btn_back' => 'Wróć do ofert',
        'success_title' => 'Aplikacja wysłana!',
        'success_msg' => 'Dziękujemy za zainteresowanie. Skontaktujemy się z Tobą wkrótce.',
        'error_title' => 'Błąd',
        'error_msg' => 'Coś poszło nie tak. Spróbuj ponownie.',
        'job_not_found' => 'Oferta pracy nie została znaleziona.',
        'required_field' => 'To pole jest wymagane.',
    ],
    'nl' => [
        'page_title' => 'Solliciteer op een baan',
        'job_title' => 'Functie',
        'your_name' => 'Uw naam',
        'your_email' => 'Uw e-mailadres',
        'your_phone' => 'Uw telefoonnummer',
        'your_message' => 'Bericht (optioneel)',
        'btn_send' => 'Sollicitatie verzenden',
        'btn_back' => 'Terug naar vacatures',
        'success_title' => 'Sollicitatie verzonden!',
        'success_msg' => 'Dank je voor je interesse. We zullen binnenkort contact met je opnemen.',
        'error_title' => 'Fout',
        'error_msg' => 'Er ging iets mis. Probeer het opnieuw.',
        'job_not_found' => 'De functie is niet gevonden.',
        'required_field' => 'Dit veld is verplicht.',
    ],
    'en' => [
        'page_title' => 'Apply for Position',
        'job_title' => 'Position',
        'your_name' => 'Your Name',
        'your_email' => 'Your Email',
        'your_phone' => 'Your Phone',
        'your_message' => 'Message (optional)',
        'btn_send' => 'Send Application',
        'btn_back' => 'Back to Jobs',
        'success_title' => 'Application Sent!',
        'success_msg' => 'Thank you for your interest. We will contact you soon.',
        'error_title' => 'Error',
        'error_msg' => 'Something went wrong. Please try again.',
        'job_not_found' => 'Job position not found.',
        'required_field' => 'This field is required.',
    ],
];

function t($key) {
    global $translations, $current_lang;
    return $translations[$current_lang][$key] ?? $translations['en'][$key] ?? $key;
}

// Pobierz szczegóły oferty
$job = null;
$job_id = isset($_GET['job_id']) ? (int)$_GET['job_id'] : 0;

if ($job_id > 0) {
    try {
        $stmt = $pdo->prepare("SELECT id, title_$current_lang as title_local, title_en, employer_name, salary_min FROM job_offers WHERE id = ? AND status = 'active'");
        $stmt->execute([$job_id]);
        $job = $stmt->fetch(PDO::FETCH_ASSOC);
    } catch(PDOException $e) {
        // ignore
    }
}

$message = '';
$success = false;

// Obsługa submitu formularza
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $job) {
    $name = trim($_POST['name'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $phone = trim($_POST['phone'] ?? '');
    $msg = trim($_POST['message'] ?? '');

    // Walidacja
    $errors = [];
    if (!$name) $errors[] = t('required_field') . ' (name)';
    if (!$email || !filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = t('required_field') . ' (email)';
    if (!$phone) $errors[] = t('required_field') . ' (phone)';

    if (empty($errors)) {
        // Log aplikacji do bazy (tabelę applications lub custom logging)
        try {
            $log_stmt = $pdo->prepare("INSERT INTO applications (job_id, applicant_name, applicant_email, applicant_phone, message, applied_at, ip_address, language) VALUES (?, ?, ?, ?, ?, NOW(), ?, ?)");
            $ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
            $log_stmt->execute([$job_id, $name, $email, $phone, $msg, $ip, $current_lang]);
        } catch(PDOException $e) {
            // Jeśli tabela nie istnieje, możemy logować do pliku
            $log_data = json_encode([
                'job_id' => $job_id,
                'name' => $name,
                'email' => $email,
                'phone' => $phone,
                'message' => $msg,
                'ip' => $_SERVER['REMOTE_ADDR'] ?? 'unknown',
                'lang' => $current_lang,
                'timestamp' => date('Y-m-d H:i:s')
            ]);
            file_put_contents(__DIR__ . '/logs/applications.log', $log_data . "\n", FILE_APPEND | LOCK_EX);
        }

        // Wyślij e-mail do admina (Beata)
        $subject = "Nowa aplikacja na stanowisko: " . ($job['title_local'] ?? $job['title_en']);
        $headers = "From: noreply@hrconsultingpartner.nl\r\n";
        $headers .= "Content-Type: text/html; charset=utf-8\r\n";

        $body = "<html><body style=\"font-family: Arial, sans-serif; color: #333;\">";
        $body .= "<h2>Nowa aplikacja na stanowisko</h2>";
        $body .= "<p><strong>Stanowisko:</strong> " . htmlspecialchars($job['title_local'] ?? $job['title_en']) . "</p>";
        $body .= "<p><strong>Pracodawca:</strong> " . htmlspecialchars($job['employer_name'] ?? 'Nieznany') . "</p>";
        $body .= "<hr>";
        $body .= "<p><strong>Imię i nazwisko:</strong> " . htmlspecialchars($name) . "</p>";
        $body .= "<p><strong>E-mail:</strong> <a href=\"mailto:" . htmlspecialchars($email) . "\">" . htmlspecialchars($email) . "</a></p>";
        $body .= "<p><strong>Telefon:</strong> <a href=\"tel:" . htmlspecialchars($phone) . "\">" . htmlspecialchars($phone) . "</a></p>";
        if ($msg) {
            $body .= "<p><strong>Wiadomość:</strong></p>";
            $body .= "<p>" . nl2br(htmlspecialchars($msg)) . "</p>";
        }
        $body .= "<hr>";
        $body .= "<p><small>Aplikacja złożona z IP: " . htmlspecialchars($_SERVER['REMOTE_ADDR'] ?? 'unknown') . " | Język: " . htmlspecialchars($current_lang) . "</small></p>";
        $body .= "</body></html>";

        @mail($admin_email, $subject, $body, $headers);

        // Wyślij potwierdzenie do kandydata
        $confirmation_subject = "Potwierdzenie aplikacji - " . ($job['title_local'] ?? $job['title_en']);
        $confirmation_body = "<html><body style=\"font-family: Arial, sans-serif; color: #333;\">";
        $confirmation_body .= "<h2>Dziękujemy za aplikację!</h2>";
        $confirmation_body .= "<p>Otrzymaliśmy Twoją aplikację na stanowisko:</p>";
        $confirmation_body .= "<p><strong>" . htmlspecialchars($job['title_local'] ?? $job['title_en']) . "</strong></p>";
        $confirmation_body .= "<p>Skontaktujemy się z Tobą wkrótce na adres e-mail: <strong>" . htmlspecialchars($email) . "</strong></p>";
        $confirmation_body .= "<p>Możesz również skontaktować się z nami:</p>";
        $confirmation_body .= "<p>📞 <a href=\"tel:+31657558110\">+31 6 5755 8110</a> (WhatsApp)</p>";
        $confirmation_body .= "<p>📧 <a href=\"mailto:beata@hrconsultingpartner.nl\">beata@hrconsultingpartner.nl</a></p>";
        $confirmation_body .= "<hr>";
        $confirmation_body .= "<p><small>" . $site_name . "</small></p>";
        $confirmation_body .= "</body></html>";

        @mail($email, $confirmation_subject, $confirmation_body, $headers);

        $success = true;
        $message = t('success_msg');
    } else {
        $message = implode(", ", $errors);
    }
}

?>
<!DOCTYPE html>
<html lang="<?php echo $current_lang; ?>">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo t('page_title'); ?> - HR Consulting Partner</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }
        .container {
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 600px;
            width: 100%;
            padding: 3rem;
        }
        .back-link {
            display: inline-block;
            margin-bottom: 2rem;
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
        }
        .back-link:hover {
            color: #764ba2;
        }
        .back-link i {
            margin-right: 0.5rem;
        }
        h1 {
            color: #333;
            margin-bottom: 0.5rem;
            font-size: 2rem;
        }
        .job-info {
            background: #f8f9ff;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            border-left: 4px solid #667eea;
        }
        .job-info h3 {
            color: #667eea;
            font-size: 1rem;
            margin-bottom: 0.25rem;
        }
        .job-info p {
            color: #666;
            margin: 0.25rem 0;
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #333;
            font-weight: 600;
            font-size: 0.95rem;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        textarea {
            width: 100%;
            padding: 0.75rem 1rem;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-family: inherit;
            font-size: 1rem;
            transition: all 0.3s;
        }
        input[type="text"]:focus,
        input[type="email"]:focus,
        input[type="tel"]:focus,
        textarea:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        textarea {
            resize: vertical;
            min-height: 120px;
        }
        .form-actions {
            display: flex;
            gap: 1rem;
            margin-top: 2rem;
        }
        button,
        .btn {
            flex: 1;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.3s;
            text-decoration: none;
            text-align: center;
            display: inline-block;
        }
        button.btn-primary {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }
        button.btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }
        .btn-secondary {
            background: #f0f0f0;
            color: #333;
        }
        .btn-secondary:hover {
            background: #e0e0e0;
        }
        .alert {
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            animation: slideIn 0.3s ease-out;
        }
        .alert-success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .alert-error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        .alert h2 {
            margin-bottom: 0.5rem;
            font-size: 1.25rem;
        }
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .required {
            color: #dc3545;
        }
    </style>
</head>
<body>
    <div class="container">
        <a href="job-board2.php?lang=<?php echo $current_lang; ?>" class="back-link">
            <i class="fas fa-arrow-left"></i>
            <?php echo t('btn_back'); ?>
        </a>

        <?php if (!$job && !$success): ?>
            <div class="alert alert-error">
                <h2><?php echo t('error_title'); ?></h2>
                <p><?php echo t('job_not_found'); ?></p>
            </div>
        <?php elseif ($success): ?>
            <div class="alert alert-success">
                <h2><?php echo t('success_title'); ?></h2>
                <p><?php echo t('success_msg'); ?></p>
            </div>
            <div style="text-align: center; margin-top: 2rem;">
                <a href="job-board2.php?lang=<?php echo $current_lang; ?>" class="btn btn-primary">
                    <i class="fas fa-briefcase"></i>
                    <?php echo t('btn_back'); ?>
                </a>
            </div>
        <?php else: ?>
            <h1><?php echo t('page_title'); ?></h1>

            <?php if ($job): ?>
                <div class="job-info">
                    <h3><?php echo t('job_title'); ?></h3>
                    <p><strong><?php echo htmlspecialchars($job['title_local'] ?? $job['title_en']); ?></strong></p>
                    <p><?php echo htmlspecialchars($job['employer_name'] ?? 'HR Consulting Partner'); ?></p>
                    <?php if ($job['salary_min']): ?>
                        <p>💰 Od €<?php echo number_format($job['salary_min'], 0); ?>/tydzień</p>
                    <?php endif; ?>
                </div>
            <?php endif; ?>

            <?php if ($message && !$success): ?>
                <div class="alert alert-error">
                    <p><?php echo htmlspecialchars($message); ?></p>
                </div>
            <?php endif; ?>

            <form method="POST" action="">
                <div class="form-group">
                    <label for="name">
                        <?php echo t('your_name'); ?>
                        <span class="required">*</span>
                    </label>
                    <input type="text" id="name" name="name" required value="<?php echo htmlspecialchars($_POST['name'] ?? ''); ?>">
                </div>

                <div class="form-group">
                    <label for="email">
                        <?php echo t('your_email'); ?>
                        <span class="required">*</span>
                    </label>
                    <input type="email" id="email" name="email" required value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>">
                </div>

                <div class="form-group">
                    <label for="phone">
                        <?php echo t('your_phone'); ?>
                        <span class="required">*</span>
                    </label>
                    <input type="tel" id="phone" name="phone" required value="<?php echo htmlspecialchars($_POST['phone'] ?? ''); ?>">
                </div>

                <div class="form-group">
                    <label for="message"><?php echo t('your_message'); ?></label>
                    <textarea id="message" name="message"><?php echo htmlspecialchars($_POST['message'] ?? ''); ?></textarea>
                </div>

                <div class="form-actions">
                    <button type="submit" class="btn-primary">
                        <i class="fas fa-paper-plane"></i>
                        <?php echo t('btn_send'); ?>
                    </button>
                    <a href="job-board2.php?lang=<?php echo $current_lang; ?>" class="btn btn-secondary">
                        <i class="fas fa-times"></i>
                        <?php echo t('btn_back'); ?>
                    </a>
                </div>
            </form>
        <?php endif; ?>
    </div>
</body>
</html>
