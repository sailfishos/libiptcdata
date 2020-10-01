Name:       libiptcdata
Summary:    IPTC tag library
Version:    1.0.5
Release:    1
License:    LGPLv2
URL:        https://github.com/ianw/libiptcdata
Source0:    %{name}-%{version}.tar.gz
Patch0:     disable-gtk-doc.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  libtool

%description
libiptcdata is a library, written in C, for manipulating the International 
Press Telecommunications Council (IPTC) metadata stored within multimedia 
files such as images. This metadata can include captions and keywords, 
often used by popular photo management applications. The library provides 
routines for parsing, viewing, modifying, and saving this metadata. 
The library is licensed under the GNU Library General Public License 
(GNU LGPL). The libiptcdata package also includes a command-line utility, 
iptc, for editing IPTC data in JPEG files, as well as Python bindings.

%package devel
Summary:    Headers and libraries for libiptcdata application development
Requires:   %{name} = %{version}-%{release}

%description devel
The libiptcdata-devel package contains the libraries and include 
files that you can use to develop libiptcdata applications.

%package python
Summary:    Python bindings for libiptcdata
Requires:   %{name} = %{version}-%{release}
Requires:   python3-devel

%description python
The libiptcdata-python package contains a Python module that allows Python 
applications to use the libiptcdata API for reading and writing IPTC 
metadata in images.

%package doc
Summary:   Documentation for %{name}
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}

%description doc
Documentation and python examples for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
export PYTHON_VERSION=%python3_version
%autogen --disable-static \
    --disable-gtk-doc \
    --enable-python
%make_build

%install
%make_install

%find_lang iptc --all-name

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/python/examples
install -m0644 python/README %{buildroot}%{_docdir}/%{name}-%{version}/python
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version}/python/examples \
        python/examples/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f iptc.lang
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/*
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libiptcdata

%files python
%defattr(-,root,root,-)
%{python3_sitearch}/*.so

%files doc
%defattr(-,root,root,-)
%doc README AUTHORS ChangeLog NEWS
%{_docdir}/%{name}-%{version}/python
