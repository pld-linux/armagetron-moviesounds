Summary:	Moviesounds addon for armagetron game
Summary(pl):	Dodatek Moviesounds do gry armagetron
Name:		armagetron-moviesounds
Version:	1
Release:	1
License:	not distributable
Group:		X11/Applications/Games
Source0:	http://armagetron.sourceforge.net/addons/moviesounds_fq.zip
# Source0-md5:	3c5d04af52eb296cdeb2fba5ecbd8899
NoSource:	0
URL:		http://armagetron.sourceforge.net/
Requires:	armagetron
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moviesounds addon for armagetron game.

Note: These files are not under the GPL; it probably is a violation of
Disney's copyright to download them.

%description -l pl
Dodatek Moviesounds do gry armagetron.

Uwaga: Te pliki nie s± objête licencj± GPL. ¦ci±gniêcie tych plików
jest prawdopodobnie naruszeniem praw autorskich Disney'a.

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
