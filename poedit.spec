Summary:	Gettext catalogs editor
Name:		poedit
Version:	1.1.5
Release:	1
License:	BSD license
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	http://prdownloads.sourcefoge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-wxwin-2.3.1.patch
URL:		http://poedit.sourceforge.net
BuildRequires:	wxGTK-devel >= 2.3.1
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gettext-devel
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

%prep
%setup -q
%patch0 -p1

%build
gettextize -c -f
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	-C src \
	DESTDIR=$RPM_BUILD_ROOT \
	install

install -d $RPM_BUILD_ROOT/%{_pixmapsdir}
install -d $RPM_BUILD_ROOT/%{_datadir}/icons
install src/appicon.xpm $RPM_BUILD_ROOT/%{_pixmapsdir}/poedit.xpm
install src/appicon.xpm $RPM_BUILD_ROOT/%{_datadir}/icons/poedit.xpm

gzip -9nf NEWS LICENSE README AUTHORS

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.html docs/img
%attr(755, root, root) %{_bindir}/poedit
%dir %{_datadir}/poedit
%{_datadir}/poedit/*
%{_datadir}/icons/poedit.xpm
%{_pixmapsdir}/poedit.xpm
