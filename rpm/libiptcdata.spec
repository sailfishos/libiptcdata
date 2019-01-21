Name:       libiptcdata
Summary:    IPTC tag library
Version:    1.0.4
Release:    1
Group:      Development/Libraries
License:    LGPLv2
URL:        http://libiptcdata.sourceforge.net/
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  python-devel
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
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The libiptcdata-devel package contains the libraries and include 
files that you can use to develop libiptcdata applications.

%package python
Summary:    Python bindings for libiptcdata
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   python-devel

%description python
The libiptcdata-python package contains a Python module that allows Python 
applications to use the libiptcdata API for reading and writing IPTC 
metadata in images.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Documentation and python examples for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static \
    --enable-python

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%find_lang iptc --all-name

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/python/examples
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        AUTHORS ChangeLog NEWS README
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
%{python_sitearch}/*.so

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
%doc %{_datadir}/gtk-doc/html/libiptcdata
