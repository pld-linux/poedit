Summary:	Gettext catalogs editor
Summary(pl.UTF-8):	Edytor katalogów gettexta
Name:		poedit
Version:	1.4.6
Release:	1
License:	MIT
Group:		X11/Applications/Editors
Source0:	http://dl.sourceforge.net/poedit/%{name}-%{version}.tar.gz
# Source0-md5:	82d665b5f6e7b0e1cec965890c784845
Patch0:		%{name}-desktop.patch
URL:		http://poedit.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gtk+2-devel
BuildRequires:	gtkspell-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	wxGTK2-unicode-devel >= 2.8.0
BuildRequires:	wxWidgets-utils
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
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
%patch0 -p1

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

%{__make} install \
	EXTRADIR="" \
	DESTDIR=$RPM_BUILD_ROOT

# fix/update locale names
install -d $RPM_BUILD_ROOT%{_datadir}/locale/{af,fa,pt,sq}/LC_MESSAGES
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{af_ZA/LC_MESSAGES/poedit.mo,af/LC_MESSAGES/poedit.mo}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{fa_IR/LC_MESSAGES/poedit.mo,fa/LC_MESSAGES/poedit.mo}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{pt_PT/LC_MESSAGES/poedit.mo,pt/LC_MESSAGES/poedit.mo}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{sq_AL/LC_MESSAGES/poedit.mo,sq/LC_MESSAGES/poedit.mo}


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
%doc AUTHORS COPYING NEWS README TODO
%attr(755,root,root) %{_bindir}/poedit
%{_datadir}/poedit
%{_desktopdir}/poedit.desktop
%{_pixmapsdir}/poedit.png
%{_iconsdir}/hicolor/*/*/poedit.png
%{_iconsdir}/hicolor/*/*/poedit.svg
%{_mandir}/man1/poedit.1*
