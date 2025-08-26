Summary:	Idle management daemon for Wayland
Summary(pl.UTF-8):	Demon zarządzający bezczynnością dla Waylanda
Name:		swayidle
Version:	1.8.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/swaywm/swayidle/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cbc80fb71c19a5d8d058d7cd5975d1eb
URL:		https://github.com/swaywm/swayidle
BuildRequires:	bash-completion-devel >= 1:2.0
BuildRequires:	fish-devel
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	scdoc
# or elogind-devel with -Dlogind-provider=elogind
BuildRequires:	systemd-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.27
Suggests:	swaylock
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is sway's idle management daemon, swayidle. It is compatible with
any Wayland compositor which implements the KDE idle protocol.

%description -l pl.UTF-8
Ten pakiet zawiera demona swaya zarządzającego bezczynnością -
swayidle. Jest zgodny z dowolnym kompozytorem Waylanda implementującym
protokół KDE idle.

%package -n bash-completion-swayidle
Summary:	Bash completion for swayidle
Summary(pl.UTF-8):	Bashowe dopełnianie argumentów swayidle
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-swayidle
Bash completion for swayidle.

%description -n bash-completion-swayidle -l pl.UTF-8
Bashowe dopełnianie argumentów dla swayidle.

%package -n fish-completion-swayidle
Summary:	fish-completion for swayidle
Summary(pl.UTF-8):	Dopełnianie argumentów swayidle dla powłoki fish
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	fish
BuildArch:	noarch

%description -n fish-completion-swayidle
fish-completion for swayidle.

%description -n fish-completion-swayidle -l pl.UTF-8
Dopełnianie argumentów swayidle dla powłoki fish.

%package -n zsh-completion-swayidle
Summary:	ZSH completion for swayidle
Summary(pl.UTF-8):	Dopełnianie argumentów swayidle dla ZSH
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-swayidle
ZSH completion for swayidle.

%description -n zsh-completion-swayidle -l pl.UTF-8
Dopełnianie argumentów swayidle dla ZSH.

%prep
%setup -q

%build
%meson \
	-Dlogind=enabled \
	-Dlogind-provider=systemd \
	-Dman-pages=enabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
