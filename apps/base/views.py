from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "base/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            greeting_text="We happy to see you in our greatest words 'GUESS THE NUMBER'!"
                          "Rules very easy: You must to guess the number from 0 to 100. You have 5 attempts!"
                          "Welcome! This is Yevhen Yalovenko Django base project."
                          "If you're enter non correct number - words inform about it."
                          "You have 100 points at start and wrong attempt cost -20 point."
                          "Good luck!!!",
            #
            title="Home Page",
        )

        return context


class AboutUsView(TemplateView):
    template_name = "base/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            about="This is symple console words. We just start",
            #
            title="About us",
        )

        return context
