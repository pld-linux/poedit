Summary:	Gettext catalogs editor
Summary(pl.UTF-8):	Edytor katalogów gettexta
Name:		poedit
Version:	3.3.2
Release:	2
License:	MIT
Group:		X11/Applications/Editors
Source0:	https://github.com/vslavik/poedit/releases/download/v%{version}-oss/%{name}-%{version}.tar.gz
# Source0-md5:	83b18a3e983c9444b31f1132a5039819
URL:		https://poedit.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	boost-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtkspell3-devel
BuildRequires:	lucene++-devel >= 3.0.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	wxGTK3-unicode-devel >= 3.0.3
BuildRequires:	wxWidgets-utils
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
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
%configure \
	--with-wx-config=wx-gtk3-unicode-config \
	--%{?debug:en}%{!?debug:dis}able-debug

%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install V=1 \
	DESTDIR=$RPM_BUILD_ROOT

# fix/update locale names
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/co
%{__mv} $RPM_BUILD_ROOT%{_localedir}/pt{_PT,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.md
%attr(755,root,root) %{_bindir}/poedit
%{_datadir}/poedit
%{_desktopdir}/net.poedit.Poedit.desktop
%{_desktopdir}/net.poedit.PoeditURI.desktop
%{_metainfodir}/net.poedit.Poedit.appdata.xml
%{_iconsdir}/hicolor/*/*/net.poedit.Poedit.png
%{_iconsdir}/hicolor/*/*/net.poedit.Poedit.svg
%{_mandir}/man1/poedit.1*
