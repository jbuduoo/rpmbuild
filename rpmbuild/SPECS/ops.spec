%define SOURCE_DIR ops-1.1.0
%define SOURCE_NAME %{SOURCE_DIR}.tar.gz
Name:       ops
Version:    1.1.0
Release:    1
Vendor:     ascentac
Summary:    OPS X86_64
License:    ascentac
Source0:    ops-1.1.0.tar.gz
%description
OPS package


%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %buildroot/tmp
cp %{SOURCE0} %buildroot/tmp


%clean
rm -rf %{buildroot}
%post
cd /tmp
tar zxvf %{SOURCE_NAME} > /dev/null
cd %{SOURCE_DIR}
fileName=$(date +/tmp/ops_"%s".log)
./install.sh > /dev/null
cd ..
rm -rf %{SOURCE_DIR}
> %{SOURCE0}
%files
/tmp/%{SOURCE_NAME}
%defattr (-,root,root)
%postun
service opsdb stop
service opsweb stop
rm -rf /opt/ops
/sbin/chkconfig --del opsweb
/sbin/chkconfig --del opsdb
rm -f /etc/init.d/opsweb
rm -f /etc/init.d/opsdb

