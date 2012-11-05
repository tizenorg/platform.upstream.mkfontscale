Name:           mkfontscale
Version:        1.1.0
Release:        1
License:        MIT
Summary:        Utility to create index of scalable font files for X
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by the
legacy X11 font system.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/mkfontscale
%{_mandir}/man1/mkfontscale.1%{?ext_man}

%changelog
