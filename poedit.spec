# TODO:
# - install GNOME and KDE releated files (MIME files)
Summary:	Gettext catalogs editor
Summary(pl):	Edytor katalogów gettexta
Name:		poedit
Version:	1.2.4
Release:	0.2
License:	BSD
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	24935b35ddb32c90fef4d0dee7a44a61
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-system_libs.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://poedit.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	wxGTK2-unicode-devel >= 2.4.0-0.8
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

%description -l pl
poEdit jest wieloplatformowym edytorem katalogów gettexta (plików
.po). U¿ywa toolkitu wxWindows, wiêc mo¿e dzia³aæ pod Uniksem oraz pod
Windows. Mo¿liwo¶ci programu to: obs³uga UTF-8, pod¶wietlanie rekordów
nie przet³umaczonych i niepewnych ("fuzzy"), pod¶wietlanie odstêpów,
przegl±darka odwo³añ, edycja nag³ówków, tworzenie nowych katalogów
oraz uaktualnianie istniej±cych z plików ¼ród³owych przez jedno
klikniêcie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-transmem \
	--with-wx-config=wxgtk2u-2.4-config \
	--%{?debug:en}%{!?debug:dis}able-debug	

%{__make} \
	EXTRADIR="" \
	gizmoslib="-lwx_gtk2u_gizmos-2.4" \
	xrclib="-lwx_gtk2u_xrc-2.4" \
	expatlib="-lexpat"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
#%doc NEWS LICENSE README AUTHORS docs/*.html docs/img
%attr(755,root,root) %{_bindir}/poedit
%{_datadir}/poedit
%{_datadir}/mime-info/%{name}*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man1/*
