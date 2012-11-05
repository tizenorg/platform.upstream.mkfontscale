#
# spec file for package mkfontscale
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           mkfontscale
Version:        1.1.0
Release:        1
License:        MIT
Summary:        Utility to create index of scalable font files for X
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM mkfontscale-skip_symlinks.diff fdo#48639 -- Ignore symlinks pointing to files in the same directory
Patch0:         mkfontscale-skip_symlinks.diff
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

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
