Summary:	Gettext catalogs editor
Summary(pl):	Edytor katalogów gettexta
Name:		poedit
Version:	1.1.9
Release:	2
License:	BSD
Group:		Applications/Editors
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-wxwin-2.3.1.patch
URL:		http://poedit.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	wxGTK-devel >= 2.3.2-5
Requires:	gettext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
.po). U¿ywa toolkitu wxWindows, wiêc mo¿e dzia³aæ pod uniksem oraz pod
Windows. Mo¿liwo¶ci programu to: obs³uga UTF-8, pod¶wietlanie rekordów
nie przet³umaczonych i "fuzzy", pod¶wietlanie odstêpów, przegl±darka
odwo³añ, edycja nag³ówków, tworzenie nowych katalogów oraz
uaktualnianie istniej±cych z plików ¼ród³owych przez jedno klikniêcie.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Development}

%{__make} install -C src \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install src/appicon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/poedit.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS LICENSE README AUTHORS docs/*.html docs/img
%attr(755,root,root) %{_bindir}/poedit
%{_datadir}/poedit
%{_applnkdir}/Development/*
%{_pixmapsdir}/*
