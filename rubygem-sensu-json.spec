# Generated from sensu-json-1.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-json

Name:           rubygem-%{gem_name}
Version:        XXX
Release:        1%{?dist}
Summary:        The Sensu JSON parser abstraction library
Group:          Development/Languages
License:        MIT
URL:            https://github.com/sensu/sensu-json
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
%if 0%{?fedora} > 21
BuildRequires:  rubygem(rspec2)
%else
BuildRequires:  rubygem(rspec)
%endif
BuildRequires:  rubygem(oj)

Requires:       rubygem(oj)

BuildArch:      noarch

%if 0%{?rhel} > 0
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
The Sensu JSON parser abstraction library.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%if 0%{?dlrn} > 0
%setup -q -D -T -n  %{dlrn_nvr}
%else
%setup -q -D -T -n  %{gem_name}-%{version}
%endif
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# relax oj dependency
sed 's/spec.add_dependency\(.*\)"oj", "[><= ]*\([^><=]*\)"\(.*\)/spec.add_dependency\1"oj", ">= \2"\3/g' %{gem_name}.gemspec
find lib -type f -exec sed -i 's/gem "oj", "[><= ]*\([^><=]*\)"/gem "oj", ">= \1"/g' {} +


%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


# Run the test suite
%check
pushd .%{gem_instdir}
%if 0%{?fedora} > 21
rspec2 -Ilib spec
%else
rspec -Ilib spec
%endif
popd


%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/sensu-json.gemspec

%changelog
