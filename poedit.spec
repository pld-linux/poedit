# TODO:
# - install GNOME and KDE releated files (MIME files)
Summary:	Gettext catalogs editor
Summary(pl.UTF-8):	Edytor katalogów gettexta
Name:		poedit
Version:	1.3.6
Release:	0.1
License:	BSD
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/poedit/%{name}-%{version}.tar.gz
# Source0-md5:	01bab36f3065daf9dcddb5dedd7c7143
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://poedit.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	gtkspell-devel
BuildRequires:	wxGTK2-unicode-devel >= 2.6.0
BuildRequires:	zip
Requires:	gettext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
poEdit is cross-platform gettext catalogs (.po files) editor. It is
built with wxWindows toolkit and can run on Unix or Windows. It aims
to provide convenient way of editing gettext catalogs. It features
UTF-8 support, fuzzy and untranslated records highlighting,
whitespaces highlighting, references browser, headers editing and can
be used to create new catalogs or update existing catalogs from source
code by single click.

%description -l pl.UTF-8
poEdit jest wieloplatformowym edytorem katalogów gettexta (plików
.po). Używa toolkitu wxWindows, więc może działać pod Uniksem oraz pod
Windows. Możliwości programu to: obsługa UTF-8, podświetlanie rekordów
nie przetłumaczonych i niepewnych ("fuzzy"), podświetlanie odstępów,
przeglądarka odwołań, edycja nagłówków, tworzenie nowych katalogów
oraz uaktualnianie istniejących z plików źródłowych przez jedno
kliknięcie.

%prep
%setup -q

%build
%{__aclocal} -I admin
%{__autoconf}
%{__automake}
%configure \
	--disable-transmem \
	--with-wx-config=wx-gtk2-unicode-config \
	--%{?debug:en}%{!?debug:dis}able-debug

%{__make} \
	EXTRADIR="" \
	expatlib="-lexpat"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_datadir}/mime-info/}

%{__make} install \
	EXTRADIR="" \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install install/poedit.{mime,keys} $RPM_BUILD_ROOT%{_datadir}/mime-info/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
#%doc NEWS LICENSE README AUTHORS docs/*.html docs/img
%attr(755,root,root) %{_bindir}/poedit
%{_datadir}/poedit
%{_datadir}/mime-info/%{name}*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
