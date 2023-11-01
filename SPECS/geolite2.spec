%global _docdir_fmt %{name}
%global _description \
GeoLite2 databases are free IP geolocation databases comparable to, but less\
accurate than, MaxMind's GeoIP2 databases.  This product includes GeoLite2 data\
created by MaxMind, available from http://www.maxmind.com.

Name:           geolite2
Version:        20180605
Release:        1%{?dist}
Summary:        Free IP geolocation databases
License:        CC-BY-SA
URL:            https://dev.maxmind.com/geoip/geoip2/geolite2/
Source0:        https://geolite.maxmind.com/download/geoip/database/GeoLite2-City_%{version}.tar.gz
Source1:        https://geolite.maxmind.com/download/geoip/database/GeoLite2-Country_%{version}.tar.gz
BuildArch:      noarch


%description %{_description}


%package city
Summary:        Free IP geolocation city database

%description city %{_description}


%package country
Summary:        Free IP geolocation country database

%description country %{_description}


%prep
%setup -q -T -c -a 0 -a 1


%install
for db in GeoLite2-City GeoLite2-Country; do
    install -D -p -m 0644 ${db}_%{version}/$db.mmdb %{buildroot}%{_datadir}/GeoIP/$db.mmdb
done


%files city
%license GeoLite2-City_%{version}/COPYRIGHT.txt GeoLite2-City_%{version}/LICENSE.txt
%dir %{_datadir}/GeoIP
%verify(not md5 size mtime) %{_datadir}/GeoIP/GeoLite2-City.mmdb


%files country
%license GeoLite2-Country_%{version}/COPYRIGHT.txt GeoLite2-Country_%{version}/LICENSE.txt
%dir %{_datadir}/GeoIP
%verify(not md5 size mtime) %{_datadir}/GeoIP/GeoLite2-Country.mmdb


%changelog
* Mon Jun 11 2018 Carl George <carl@george.computer> - 20180605-1
- Latest upstream

* Tue Apr 24 2018 Carl George <carl@george.computer> - 20180403-1
- Initial package
