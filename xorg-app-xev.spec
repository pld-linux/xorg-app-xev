Summary:	xev application - printing contents of X events
Summary(pl.UTF-8):	Aplikacja xev wypisujaca zawartość zdarzeń X
Name:		xorg-app-xev
Version:	1.2.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xev-%{version}.tar.xz
# Source0-md5:	61219e492511b3d78375da76defbdc97
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.2
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libXrandr >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xev application creates a window and then asks the X server to send it
events whenever anything happens to the window (such as it being
moved, resized, typed in, clicked in, etc.). You can also attach it to
an existing window. It is useful for seeing what causes events to
occur and to display the information that they contain; it is
essentially a debugging and development tool, and should not be needed
in normal usage.

%description -l pl.UTF-8
Aplikacja xev tworzy okno i żąda od serwera X przesyłania do siebie
wszystkich zdarzeń występujących w tym oknie (takich jak przesunięcia,
zmiana rozmiaru, naciśnięcia klawiszy, kliknięcia). Może także
podłączyć się do istniejącego okna. Jest przydatna do sprawdzania co
powoduje występowanie zdarzeń i wyświetlania zawartych w nich
informacji; jest to zasadnicze narzędzie diagnostyczne i
programistyczne, natomiast nie powinno być potrzebne przy zwykłym
użytkowaniu systemu.

%prep
%setup -q -n xev-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xev
%{_mandir}/man1/xev.1*
