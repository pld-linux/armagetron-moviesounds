Summary:	Moviesounds addon for armagetron game
Summary(pl.UTF-8):	Dodatek Moviesounds do gry armagetron
Name:		armagetron-moviesounds
Version:	1
Release:	1
License:	not distributable
Group:		X11/Applications/Games
Source0:	http://armagetron.sourceforge.net/addons/moviesounds_fq.zip
# NoSource0-md5: 3c5d04af52eb296cdeb2fba5ecbd8899
NoSource:	0
URL:		http://armagetron.sourceforge.net/addons.html
BuildRequires:	unzip
Requires:	armagetron
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moviesounds addon for armagetron game.

Note: These files are not under the GPL; it probably is a violation of
Disney's copyright to download them.

%description -l pl.UTF-8
Dodatek Moviesounds do gry armagetron.

Uwaga: Te pliki nie są objęte licencją GPL. Ściągnięcie tych plików
jest prawdopodobnie naruszeniem praw autorskich Disneya.

%prep
%setup -q -n moviesounds

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/games/armagetron/moviesounds

install *.wav $RPM_BUILD_ROOT%{_prefix}/games/armagetron/moviesounds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/games/armagetron/moviesounds
