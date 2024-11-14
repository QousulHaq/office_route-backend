// === JQuery Audio Sign In === //
$(document).ready(function() {
  // Ambil elemen tombol Sign In di Navbar dan audio Sign In di Navbar
  const navbarSigninButton = $(".btn-signin");
  const navbarSigninSound = $("#navbarSigninSound")[0]; // Mengakses elemen audio DOM dengan jQuery

  // Tambah event listener untuk memutar suara saat tombol Sign In di Navbar diklik
  navbarSigninButton.on("click", function(event) {
      event.preventDefault(); // Mencegah halaman langsung berganti sebelum suara diputar

      // Cek apakah file audio ada dan siap diputar
      if (navbarSigninSound) {
          navbarSigninSound.play().then(function() {
              // Tunggu suara selesai diputar baru alihkan halaman
              setTimeout(function() {
                  window.location.href = "login.html";
              }, 1500); // Durasi menunggu sebelum pindah halaman
          }).catch(function(error) {
              console.error("Gagal memutar audio:", error);
              // Langsung alihkan halaman jika gagal memutar suara
              window.location.href = "login.html";
          });
      } else {
          console.error("Audio tidak ditemukan");
          window.location.href = "login.html"; // Tetap alihkan halaman jika audio tidak ada
      }
  });
});

// === JQuery FAQs === //
$(document).ready(function () {
  // Memilih semua tombol accordion dengan kelas '.accordion-button'
  var accordionButtons = $(".accordion-button");

  // Melakukan loop pada semua tombol untuk menambahkan event listener
  accordionButtons.each(function () {
    var button = $(this);

    // Menambahkan event listener 'mouseover' untuk mengubah warna background dan teks saat kursor diarahkan
    button.on("mouseover", function () {
      button.css({
        "background-color": "#1E3A8A", // Mengubah warna background menjadi #1E3A8A
        color: "white", // Mengubah warna teks menjadi putih
      });
    });

    // Menambahkan event listener untuk mengembalikan warna background dan teks saat kursor dijauhkan
    button.on("mouseout", function () {
      button.css({
        "background-color": "", // Mengembalikan warna background ke warna semula (default)
        color: "", // Mengembalikan warna teks ke warna semula (default)
      });
    });
  });
});

// === JQuery Back to Top === //
$(document).ready(function () {
  // Mengecek posisi scroll saat halaman di-refresh
  if ($(this).scrollTop() < 200) {
    $("#backToTop").hide(); // Pastikan button disembunyikan jika posisi scroll kurang dari 200px
  }

  // Saat pengguna scroll halaman
  $(window).scroll(function () {
    if ($(this).scrollTop() > 200) {
      // Jika sudah scroll lebih dari 200px, tampilkan button
      $("#backToTop").fadeIn();
    } else {
      // Jika tidak, sembunyikan button
      $("#backToTop").fadeOut();
    }
  });

  // Saat button diklik, kembali ke atas
  $("#backToTop").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 150); // Scroll cepat dalam 150ms
    return false; // Mencegah aksi default
  });
});

// === JQuery Validasi Login === //
$(document).ready(function () {
  // submit form dg jquery
  $("#loginForm").submit(function (event) {
    event.preventDefault();
    var email = $("#email").val();
    var password = $("#password").val();

    // validasi
    if (email === "" || password === "") {
      alert("Please fill in all fields.");
    } else {
      alert("Form submitted successfully! Redirecting to homepage...");
      window.location.href = "index.html";
    }
  });
});

// === JQuery Validasi Sign Up === //
$(document).ready(function () {
  // submit form dg jquery
  $("#SignupForm").submit(function (event) {
    event.preventDefault();
    var name = $("#name").val();
    var email = $("#email").val();
    var password = $("#password").val();

    // validasi
    if (name === "" || email === "" || password === "") {
      alert("Please fill in all fields.");
    } else {
      alert("Form submitted successfully! Redirecting to login...");
      window.location.href = "login.html";
    }
  });
});

// === JQuery Eye cek Password === //
$("#togglePassword").click(function () {
var passwordField = $("#password");
var passwordFieldType = passwordField.attr("type");

// Jika tipe input password, ubah menjadi teks
if (passwordFieldType === "password") {
  passwordField.attr("type", "text");
  $(this).removeClass("bi-eye").addClass("bi-eye-slash"); // Ganti ikon menjadi "mata tertutup"
} else {
  passwordField.attr("type", "password");
  $(this).removeClass("bi-eye-slash").addClass("bi-eye"); // Ganti ikon kembali menjadi "mata terbuka"
}
});



