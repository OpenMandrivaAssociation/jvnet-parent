Name:           jvnet-parent
Version:        5
Release:        1
Summary:        Java.net parent POM file


License:        ASL 2.0
URL:            https://www.java.net
Source0:        https://repo1.maven.org/maven2/net/java/%{name}/%{version}/%{name}-%{version}.pom
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption:	validate


%description
Java.net parent POM file used by most Java.net subprojects such as
Glassfish

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%files -f .mfiles
%doc LICENSE
