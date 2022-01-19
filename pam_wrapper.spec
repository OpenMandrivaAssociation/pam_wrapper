%global major 0
%define libname %mklibname pam_wrapper %major
%define devname %mklibname pam_wrapper -d

%define testlibname %mklibname pamtest %major
%define testdevname %mklibname pamtest -d

Name:           pam_wrapper
Version:        1.1.4
Release:        1

Summary:        A tool to test PAM applications and PAM modules
License:        GPLv3+
Url:            http://cwrap.org/
Group:          Development/Other
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(python)
BuildRequires:  pam-devel
BuildRequires:  doxygen
BuildRequires:  git

Recommends:     cmake
Recommends:     pkgconfig

Requires:       %{libname} = %version-%release

%description
This component of cwrap allows you to either test your PAM (Linux-PAM
and OpenPAM) application or module.

For testing PAM applications, simple PAM module called pam_matrix is
included. If you plan to test a PAM module you can use the pamtest library,
which simplifies testing of modules. You can combine it with the cmocka
unit testing framework or you can use the provided Python bindings to
write tests for your module in Python.

%package -n %{libname}
Summary:        A tool to test PAM applications and PAM modules
License:        GPLv3+
Requires:       pam_wrapper = %{version}-%{release}

%description -n %{libname}
This component of cwrap allows you to either test your PAM (Linux-PAM
and OpenPAM) application or module.

For testing PAM applications, simple PAM module called pam_matrix is
included. If you plan to test a PAM module you can use the pamtest library,
which simplifies testing of modules. You can combine it with the cmocka
unit testing framework or you can use the provided Python bindings to
write tests for your module in Python.

%package -n %{testlibname}
Summary:        A tool to test PAM applications and PAM modules
License:        GPLv3+
Requires:       pam_wrapper = %{version}-%{release}

%description -n  %{testlibname}
If you plan to test a PAM module you can use this library, which simplifies
testing of modules.


%package -n %{testdevname}
Summary:        A tool to test PAM applications and PAM modules
License:        GPLv3+
Requires:       pam_wrapper = %{version}-%{release}
Requires:       %{testlibname} = %{version}-%{release}

Recommends:     cmake
Recommends:     pkgconfig


%description -n %{testdevname}
If you plan to develop tests for a PAM module you can use this library,
which simplifies testing of modules. This sub package includes the header
files for libpamtest.

%package -n python-libpamtest
Summary:        A python wrapper for libpamtest
License:        GPLv3+
Requires:       pam_wrapper = %{version}-%{release}
Requires:       %{testlibname} = %{version}-%{release}

%description -n python-libpamtest
If you plan to develop python tests for a PAM module you can use this
library, which simplifies testing of modules. This subpackage includes
the header files for libpamtest


%prep
%autosetup -S git


%build
%cmake \
  -DUNIT_TESTING=ON

%make_build

%install
%make_install -C build

%check
%ctest

%files
%{_libdir}/pkgconfig/pam_wrapper.pc
%{_libdir}/libpam_wrapper.so
%dir %{_libdir}/cmake/pam_wrapper
%{_libdir}/cmake/pam_wrapper/pam_wrapper-config-version.cmake
%{_libdir}/cmake/pam_wrapper/pam_wrapper-config.cmake
%{_libdir}/pam_wrapper/pam_chatty.so
%{_libdir}/pam_wrapper/pam_matrix.so
%{_libdir}/pam_wrapper/pam_get_items.so
%{_libdir}/pam_wrapper/pam_set_items.so
%{_mandir}/man1/pam_wrapper.1*
%{_mandir}/man8/pam_chatty.8*
%{_mandir}/man8/pam_matrix.8*
%{_mandir}/man8/pam_get_items.8*
%{_mandir}/man8/pam_set_items.8*

%files -n %{libname}
%{_libdir}/libpam_wrapper.so.%{major}{,.*}

%files -n %{testlibname}
%{_libdir}/libpamtest.so.%{major}{,.*}

%files -n %{testdevname}
%{_libdir}/libpamtest.so
%{_libdir}/pkgconfig/libpamtest.pc
%dir %{_libdir}/cmake/pamtest
%{_libdir}/cmake/pamtest/pamtest-config-relwithdebinfo.cmake
%{_libdir}/cmake/pamtest/pamtest-config-version.cmake
%{_libdir}/cmake/pamtest/pamtest-config.cmake
%{_includedir}/libpamtest.h

%files -n python-libpamtest
%{python_sitearch}/pypamtest.so
