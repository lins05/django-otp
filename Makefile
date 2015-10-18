SUBDIRS = django-otp django-otp-agents django-otp-twilio django-otp-yubikey

.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@
