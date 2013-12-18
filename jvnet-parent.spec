%_javapackages_macros
Name:           jvnet-parent
Version:        4
Release:        2.0%{?dist}
Summary:        Java.net parent POM file


License:        ASL 2.0
URL:            http://www.java.net
Source0:        http://repo1.maven.org/maven2/net/java/%{name}/%{version}/%{name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-enforcer-plugin


%description
Java.net parent POM file used by most Java.net subprojects such as
Glassfish

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
# we provide correct version of maven, no need to enforce and pull in dependencies
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
