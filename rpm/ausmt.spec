# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       ausmt

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    AUSMT
Version:    1.2.1
Release:    1
Group:      Qt/Qt
License:    TODO
URL:        http://github.com/SfietKonstantin/ausmt
Source0:    %{name}-%{version}.tar.bz2
Source100:  ausmt.yaml
Requires:   rpm >= 4.9.0
Requires:   patchutils
Requires:   patch
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(nemonotifications-qt5)

%description
AUSMT stands for Auto-Update System Modification Technology. AUSMT enables
patching of webOS system safely, handling the situations like OTA updates
etc.

This modified AUSMT is used by patchmanager in SailfishOS to perform system
files, just like with Preware on webOS.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
/opt/ausmt
# >> files
# << files
