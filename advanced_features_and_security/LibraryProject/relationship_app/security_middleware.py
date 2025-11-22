from django.utils.deprecation import MiddlewareMixin

class SecurityHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Prevent MIME-type sniffing
        response["X-Content-Type-Options"] = "nosniff"

        # Enable XSS protection in browsers
        response["X-XSS-Protection"] = "1; mode=block"

        # Prevent the site from being displayed in iframes
        response["X-Frame-Options"] = "DENY"

        # Basic Content Security Policy
        response["Content-Security-Policy"] = "default-src 'self'"

        return response
