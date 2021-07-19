Summary:	Idle management daemon for Wayland
Name:		swayidle
Version:	1.6
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/swaywm/swayidle/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fb24916f9c25a3c85665b3112183f097
URL:		https://github.com/swaywm/swayidle
BuildRequires:	bash-completion
BuildRequires:	fish-devel
BuildRequires:	meson >= 0.48.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc
BuildRequires:	systemd-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is sway's idle management daemon, swayidle. It is compatible with
any Wayland compositor which implements the KDE idle protocol.

%package -n bash-completion-swayidle
Summary:	Bash completion for swayidle
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0
BuildArch:	noarch

%description -n bash-completion-swayidle
Bash completion for swayidle.

%package -n fish-completion-swayidle
Summary:	fish-completion for swayidle
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	fish
BuildArch:	noarch

%description -n fish-completion-swayidle
fish-completion for swayidle.

%package -n zsh-completion-swayidle
Summary:	ZSH completion for swayidle
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-swayidle
ZSH completion for swayidle.

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/swayidle
%{_mandir}/man1/swayidle.1*

%files -n bash-completion-swayidle
%defattr(644,root,root,755)
%{bash_compdir}/swayidle

%files -n fish-completion-swayidle
%defattr(644,root,root,755)
%{fish_compdir}/swayidle.fish

%files -n zsh-completion-swayidle
%defattr(644,root,root,755)
%{zsh_compdir}/_swayidle
